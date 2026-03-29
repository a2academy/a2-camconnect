"""Mock compatibility engine: maps selected feature slugs to brand match levels."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

MatchLevel = Literal["full", "partial", "bridge"]


@dataclass(frozen=True)
class FeatureDef:
    slug: str
    label: str
    category: str


FEATURE_GROUPS: list[tuple[str, list[FeatureDef]]] = [
    (
        "Video & imaging",
        [
            FeatureDef("res_4k", "4K resolution", "Video & imaging"),
            FeatureDef("res_1080p", "1080p / Full HD", "Video & imaging"),
            FeatureDef("fps_60", "60 fps recording", "Video & imaging"),
            FeatureDef("hdr_wdr", "HDR / WDR", "Video & imaging"),
            FeatureDef("fov_wide", "Wide field of view", "Video & imaging"),
            FeatureDef("optical_zoom", "Optical zoom", "Video & imaging"),
            FeatureDef("digital_zoom", "Digital zoom", "Video & imaging"),
            FeatureDef("multi_stream", "Multi-stream / substreams", "Video & imaging"),
            FeatureDef("bitrate_ctrl", "Bitrate control", "Video & imaging"),
            FeatureDef("low_light", "Strong low-light performance", "Video & imaging"),
        ],
    ),
    (
        "Night vision",
        [
            FeatureDef("ir_night", "IR night vision", "Night vision"),
            FeatureDef("color_night", "Color night vision", "Night vision"),
            FeatureDef("starlight", "Starlight sensor", "Night vision"),
            FeatureDef("hybrid_night", "Smart hybrid night vision", "Night vision"),
            FeatureDef("long_ir", "Long-range IR", "Night vision"),
            FeatureDef("adaptive_ir", "Adaptive IR", "Night vision"),
            FeatureDef("auto_dn", "Automatic day/night switching", "Night vision"),
        ],
    ),
    (
        "AI detection",
        [
            FeatureDef("ai_person", "Person detection", "AI detection"),
            FeatureDef("ai_vehicle", "Vehicle detection", "AI detection"),
            FeatureDef("ai_animal", "Animal detection", "AI detection"),
            FeatureDef("ai_package", "Package detection", "AI detection"),
            FeatureDef("ai_face", "Face recognition", "AI detection"),
            FeatureDef("ai_lpr", "License plate (LPR/ANPR)", "AI detection"),
            FeatureDef("ai_intrusion", "Intrusion detection", "AI detection"),
            FeatureDef("ai_line", "Line crossing", "AI detection"),
            FeatureDef("ai_loiter", "Loitering detection", "AI detection"),
            FeatureDef("ai_object_lr", "Object left/removed", "AI detection"),
            FeatureDef("ai_crowd", "Crowd detection", "AI detection"),
            FeatureDef("ai_motion_cls", "Motion classification", "AI detection"),
            FeatureDef("ai_event_filter", "Smart event filtering", "AI detection"),
        ],
    ),
    (
        "Motion & zones",
        [
            FeatureDef("mot_zones", "Configurable motion zones", "Motion & zones"),
            FeatureDef("act_zones", "Activity zones", "Motion & zones"),
            FeatureDef("privacy_mask", "Privacy masking", "Motion & zones"),
            FeatureDef("det_sens", "Detection sensitivity", "Motion & zones"),
            FeatureDef("scheduling", "Scheduling rules", "Motion & zones"),
            FeatureDef("alert_thresh", "Alert thresholds", "Motion & zones"),
            FeatureDef("region_analytics", "Region-based analytics", "Motion & zones"),
            FeatureDef("smart_mot_filter", "Smart motion filtering", "Motion & zones"),
        ],
    ),
    (
        "Storage",
        [
            FeatureDef("stor_sd", "Local SD card recording", "Storage"),
            FeatureDef("stor_nvr", "NVR support", "Storage"),
            FeatureDef("stor_nas", "NAS compatibility", "Storage"),
            FeatureDef("stor_cloud", "Cloud storage", "Storage"),
            FeatureDef("stor_hybrid", "Hybrid cloud + local", "Storage"),
            FeatureDef("stor_edge", "Edge recording", "Storage"),
            FeatureDef("rec_continuous", "Continuous recording", "Storage"),
            FeatureDef("rec_event", "Event-based recording", "Storage"),
            FeatureDef("stor_redundant", "Redundant storage", "Storage"),
            FeatureDef("retention", "Retention controls", "Storage"),
        ],
    ),
    (
        "Connectivity & protocols",
        [
            FeatureDef("rtsp", "RTSP", "Connectivity & protocols"),
            FeatureDef("onvif", "ONVIF compatibility", "Connectivity & protocols"),
            FeatureDef("api", "API access", "Connectivity & protocols"),
            FeatureDef("webhooks", "Webhooks", "Connectivity & protocols"),
            FeatureDef("mqtt", "MQTT", "Connectivity & protocols"),
            FeatureDef("http_snap", "HTTP snapshot access", "Connectivity & protocols"),
            FeatureDef("ftp_upload", "FTP/SFTP upload", "Connectivity & protocols"),
            FeatureDef("poe", "PoE", "Connectivity & protocols"),
            FeatureDef("wifi", "Wi-Fi", "Connectivity & protocols"),
            FeatureDef("ethernet", "Ethernet", "Connectivity & protocols"),
            FeatureDef("vlan", "VLAN compatibility", "Connectivity & protocols"),
            FeatureDef("multi_net", "Multi-network support", "Connectivity & protocols"),
        ],
    ),
    (
        "Audio",
        [
            FeatureDef("aud_mic", "Microphone", "Audio"),
            FeatureDef("aud_2way", "Two-way audio", "Audio"),
            FeatureDef("aud_speaker", "Speaker output", "Audio"),
            FeatureDef("aud_siren", "Siren capability", "Audio"),
            FeatureDef("aud_detect", "Audio detection", "Audio"),
            FeatureDef("aud_ptt", "Push-to-talk", "Audio"),
        ],
    ),
    (
        "Smart home",
        [
            FeatureDef("sh_homekit", "Apple HomeKit", "Smart home"),
            FeatureDef("sh_google", "Google Home", "Smart home"),
            FeatureDef("sh_alexa", "Amazon Alexa", "Smart home"),
            FeatureDef("sh_ha", "Home Assistant", "Smart home"),
            FeatureDef("sh_smartthings", "SmartThings", "Smart home"),
            FeatureDef("sh_matter", "Matter support", "Smart home"),
            FeatureDef("sh_third", "Third-party automation", "Smart home"),
        ],
    ),
    (
        "Performance & system",
        [
            FeatureDef("perf_edge_ai", "Edge AI processing", "Performance & system"),
            FeatureDef("perf_low_lat", "Low latency mode", "Performance & system"),
            FeatureDef("perf_rt_alerts", "Real-time alerts", "Performance & system"),
            FeatureDef("perf_local_cloud", "Local vs cloud processing choice", "Performance & system"),
            FeatureDef("perf_multiview", "Multi-stream viewing", "Performance & system"),
            FeatureDef("perf_hw_accel", "Hardware acceleration", "Performance & system"),
            FeatureDef("perf_dash_uni", "Dashboard unification support", "Performance & system"),
        ],
    ),
    (
        "Privacy & security",
        [
            FeatureDef("priv_local", "Local-only operation", "Privacy & security"),
            FeatureDef("priv_no_cloud", "No cloud requirement", "Privacy & security"),
            FeatureDef("priv_e2e", "End-to-end encryption", "Privacy & security"),
            FeatureDef("priv_uac", "User access controls", "Privacy & security"),
            FeatureDef("priv_rbac", "Role-based permissions", "Privacy & security"),
            FeatureDef("priv_fw", "Firewall-friendly networking", "Privacy & security"),
            FeatureDef("priv_remote", "Secure remote access", "Privacy & security"),
            FeatureDef("priv_audit", "Audit logs", "Privacy & security"),
            FeatureDef("priv_data_ret", "Data retention policies", "Privacy & security"),
        ],
    ),
]

ALL_FEATURE_SLUGS = {f.slug for _, feats in FEATURE_GROUPS for f in feats}


@dataclass(frozen=True)
class BrandDef:
    slug: str
    name: str
    supported: frozenset[str]
    """Features this brand covers natively in the mock model."""
    bridge_ok: frozenset[str]
    """Features achievable via bridge / companion app — shown as Requires Bridge when selected but not in supported."""


BRANDS: list[BrandDef] = [
    BrandDef(
        "ubiquiti",
        "Ubiquiti UniFi Protect",
        frozenset(
            {
                "res_4k",
                "fps_60",
                "hdr_wdr",
                "multi_stream",
                "ai_person",
                "ai_vehicle",
                "mot_zones",
                "privacy_mask",
                "stor_nvr",
                "stor_cloud",
                "rtsp",
                "onvif",
                "poe",
                "ethernet",
                "perf_low_lat",
                "perf_rt_alerts",
                "priv_uac",
                "priv_remote",
            }
        ),
        frozenset({"sh_homekit", "sh_google", "ai_face", "stor_nas"}),
    ),
    BrandDef(
        "reolink",
        "Reolink",
        frozenset(
            {
                "res_4k",
                "res_1080p",
                "color_night",
                "ir_night",
                "ai_person",
                "ai_vehicle",
                "ai_animal",
                "stor_sd",
                "stor_nvr",
                "rtsp",
                "onvif",
                "poe",
                "wifi",
                "aud_2way",
                "sh_google",
                "sh_alexa",
            }
        ),
        frozenset({"ai_face", "ai_lpr", "stor_nas", "mqtt"}),
    ),
    BrandDef(
        "axis",
        "Axis",
        frozenset(
            {
                "res_4k",
                "hdr_wdr",
                "multi_stream",
                "ai_person",
                "ai_vehicle",
                "ai_intrusion",
                "mot_zones",
                "privacy_mask",
                "stor_edge",
                "rtsp",
                "onvif",
                "api",
                "mqtt",
                "poe",
                "perf_edge_ai",
                "priv_rbac",
                "priv_audit",
            }
        ),
        frozenset({"stor_cloud", "sh_homekit"}),
    ),
    BrandDef(
        "hikvision",
        "Hikvision",
        frozenset(
            {
                "res_4k",
                "ir_night",
                "ai_person",
                "ai_vehicle",
                "ai_face",
                "ai_lpr",
                "ai_intrusion",
                "ai_line",
                "stor_nvr",
                "stor_nas",
                "rtsp",
                "onvif",
                "poe",
                "ftp_upload",
            }
        ),
        frozenset({"sh_ha", "mqtt", "stor_cloud"}),
    ),
    BrandDef(
        "dahua",
        "Dahua",
        frozenset(
            {
                "res_4k",
                "ir_night",
                "ai_person",
                "ai_vehicle",
                "ai_intrusion",
                "stor_nvr",
                "rtsp",
                "onvif",
                "poe",
                "vlan",
            }
        ),
        frozenset({"ai_face", "stor_cloud", "mqtt"}),
    ),
    BrandDef(
        "amcrest",
        "Amcrest",
        frozenset(
            {
                "res_1080p",
                "res_4k",
                "ir_night",
                "ai_person",
                "stor_sd",
                "stor_nvr",
                "rtsp",
                "onvif",
                "poe",
                "wifi",
                "aud_mic",
            }
        ),
        frozenset({"ai_vehicle", "stor_cloud"}),
    ),
    BrandDef(
        "hanwha",
        "Hanwha Wisenet",
        frozenset(
            {
                "res_4k",
                "hdr_wdr",
                "ai_person",
                "ai_vehicle",
                "ai_face",
                "mot_zones",
                "stor_nvr",
                "rtsp",
                "onvif",
                "poe",
                "priv_rbac",
            }
        ),
        frozenset({"stor_cloud", "mqtt"}),
    ),
    BrandDef(
        "bosch",
        "Bosch",
        frozenset(
            {
                "res_4k",
                "ai_intrusion",
                "ai_line",
                "mot_zones",
                "stor_nvr",
                "rtsp",
                "onvif",
                "poe",
                "perf_low_lat",
            }
        ),
        frozenset({"stor_cloud", "sh_ha"}),
    ),
    BrandDef(
        "uniview",
        "Uniview (UNV)",
        frozenset(
            {
                "res_4k",
                "ir_night",
                "ai_person",
                "ai_vehicle",
                "stor_nvr",
                "rtsp",
                "onvif",
                "poe",
            }
        ),
        frozenset({"ai_face", "stor_cloud"}),
    ),
    BrandDef(
        "tplink_vigi",
        "TP-Link VIGI",
        frozenset(
            {
                "res_1080p",
                "ir_night",
                "ai_person",
                "stor_sd",
                "stor_cloud",
                "wifi",
                "rtsp",
                "sh_google",
                "sh_alexa",
            }
        ),
        frozenset({"onvif", "stor_nvr", "poe"}),
    ),
    BrandDef(
        "synology",
        "Synology",
        frozenset(
            {
                "stor_nas",
                "stor_nvr",
                "rtsp",
                "onvif",
                "ai_person",
                "ai_vehicle",
                "perf_dash_uni",
                "priv_local",
                "priv_no_cloud",
            }
        ),
        frozenset(
            {
                "res_4k",
                "ai_face",
                "poe",
                "mqtt",
                "sh_ha",
            }
        ),
    ),
    BrandDef(
        "eufy",
        "Eufy",
        frozenset(
            {
                "res_1080p",
                "color_night",
                "ai_person",
                "ai_package",
                "stor_local",
                "stor_cloud",
                "wifi",
                "sh_google",
                "sh_alexa",
                "sh_homekit",
            }
        ),
        frozenset(),
    ),
    BrandDef(
        "arlo",
        "Arlo",
        frozenset(
            {
                "res_1080p",
                "res_4k",
                "ir_night",
                "ai_person",
                "ai_vehicle",
                "ai_animal",
                "stor_cloud",
                "wifi",
                "sh_google",
                "sh_alexa",
            }
        ),
        frozenset({"rtsp", "onvif", "poe"}),
    ),
    BrandDef(
        "ring",
        "Ring",
        frozenset(
            {
                "res_1080p",
                "ir_night",
                "ai_person",
                "ai_package",
                "stor_cloud",
                "wifi",
                "sh_alexa",
                "aud_2way",
            }
        ),
        frozenset({"onvif", "rtsp", "stor_nvr"}),
    ),
    BrandDef(
        "wyze",
        "Wyze",
        frozenset(
            {
                "res_1080p",
                "ir_night",
                "ai_person",
                "stor_cloud",
                "wifi",
                "sh_google",
                "sh_alexa",
            }
        ),
        frozenset({"onvif", "rtsp", "stor_nvr"}),
    ),
    BrandDef(
        "foscam",
        "Foscam",
        frozenset(
            {
                "res_1080p",
                "ir_night",
                "rtsp",
                "onvif",
                "wifi",
                "poe",
                "stor_sd",
                "aud_mic",
            }
        ),
        frozenset({"ai_person", "stor_nvr"}),
    ),
    BrandDef(
        "lorex",
        "Lorex",
        frozenset(
            {
                "res_4k",
                "ir_night",
                "color_night",
                "ai_person",
                "ai_vehicle",
                "stor_nvr",
                "stor_sd",
                "poe",
                "rtsp",
            }
        ),
        frozenset({"onvif", "mqtt"}),
    ),
    BrandDef(
        "swann",
        "Swann",
        frozenset(
            {
                "res_1080p",
                "ir_night",
                "ai_person",
                "stor_nvr",
                "wifi",
                "rtsp",
            }
        ),
        frozenset({"onvif", "stor_cloud"}),
    ),
    BrandDef(
        "onvif_generic",
        "Other ONVIF-compatible cameras",
        frozenset(
            {
                "onvif",
                "rtsp",
                "res_1080p",
                "ethernet",
                "poe",
                "mot_zones",
                "stor_nvr",
            }
        ),
        frozenset(
            {
                "ai_person",
                "ai_vehicle",
                "stor_cloud",
                "mqtt",
                "sh_ha",
            }
        ),
    ),
]


def evaluate_brands(selected: set[str]) -> list[dict]:
    """Return visible brands with match levels; hides brands with weak overlap when selection is non-empty."""
    if not selected:
        return [
            {
                "slug": b.slug,
                "name": b.name,
                "level": "full",
                "matched": 0,
                "total_selected": 0,
                "native_count": 0,
                "bridge_count": 0,
            }
            for b in BRANDS
        ]

    n_sel = len(selected)
    out: list[dict] = []

    for b in BRANDS:
        native = selected & b.supported
        need_bridge = selected - b.supported
        bridge_covers = need_bridge & b.bridge_ok
        still_missing = need_bridge - bridge_covers

        if not native and not bridge_covers:
            continue

        if still_missing:
            if len(native | bridge_covers) < max(1, int(0.4 * n_sel)):
                continue

        if not still_missing:
            level: MatchLevel = "full" if native == selected else "bridge"
        elif len(still_missing) <= n_sel // 2 and (native or bridge_covers):
            level = "partial"
        else:
            level = "partial"

        covered = native | bridge_covers
        out.append(
            {
                "slug": b.slug,
                "name": b.name,
                "level": level,
                "matched": len(covered),
                "total_selected": n_sel,
                "native_count": len(native),
                "bridge_count": len(bridge_covers),
            }
        )

    out.sort(
        key=lambda r: (
            0 if r["level"] == "full" else 1 if r["level"] == "bridge" else 2,
            -r["matched"] / max(1, r["total_selected"]),
            r["name"],
        )
    )
    return out
