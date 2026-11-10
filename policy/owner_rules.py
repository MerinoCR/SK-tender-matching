"""Owner rules, 2026-11-10. Reviewed exact-SKU facts in; policy dispositions out.
Not a fact extractor, engineering confirmation, or final compliance gate.
"""
import math
VERSION = "2026-11-10.1"

def assess(topic, facts):
    if not isinstance(facts, dict) or not isinstance(facts.get("sku_id"), str) or not facts["sku_id"].strip():
        raise ValueError("exact sku_id required")
    yes = lambda key: facts.get(key) is True
    status, basis = "pending_verification", "missing_reviewed_facts"
    if topic == "load":
        rating = facts.get("specified_basis") or "static"
        if rating not in ("static", "dynamic", "safe_working"):
            raise ValueError("unsupported explicit load basis")
        actual, required = facts.get(rating + "_kg"), facts.get("required_kg")
        for value in (actual, required):
            if value is not None and (type(value) not in (int, float) or not math.isfinite(value) or value < 0):
                raise ValueError("invalid load value")
        if actual is not None and required is not None:
            status = "supported" if actual >= required else "standard_deviation"
        basis = "load_basis:" + rating
    elif topic in ("vascular_position", "corner_bumpers", "lower_storage", "cassette_travel"):
        flag = {"vascular_position": "trendelenburg", "corner_bumpers": "bumpers",
                "lower_storage": "bottom_plastic_cover", "cassette_travel": "full_body_xray"}[topic]
        if yes(flag):
            status, basis = "accepted_owner_rule", flag
    elif topic == "rigid_four_sections":
        if yes("back_adjustment") and yes("knee_adjustment"):
            status, basis = "accepted_owner_rule", "back_and_knee_adjustment"
    elif topic == "iv_pole":
        if yes("pole") and yes("mounts"):
            status, basis = "accepted_owner_rule", "corner_mounts_polished_variable_height_same_brand_pole"
    elif topic == "backrest_reach":
        status = "supported" if yes("required_range_demonstrated") else "customization_to_request"
        basis = "documented_range" if yes("required_range_demonstrated") else "owner_customization_request"
    elif topic == "antistatic_wheels":
        status, basis = "customization_to_specify", "owner_accepted_customization"
    elif topic == "rail_details":
        status, basis = "non_strict", "owner_scope_rule"
    elif topic == "fifth_wheel_diameter":
        status, basis = "pending_verification", "verify_diameter"
    elif topic == "mattress":
        status, basis = "separate_customizable_product", "owner_component_rule"
    else:
        raise ValueError("unknown topic")
    if yes("explicit_contradiction"):
        status = "conflict_review_required"
    return dict(sku_id=facts["sku_id"], topic=topic, policy_version=VERSION,
                status=status, basis=basis, source_conflict=yes("source_conflict"),
                engineering_confirmed=False, full_offer_approved=False)
