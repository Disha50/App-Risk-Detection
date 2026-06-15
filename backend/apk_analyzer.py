from androguard.misc import AnalyzeAPK

def analyze_apk(apk_path):
    a, d, dx = AnalyzeAPK(apk_path)

    permissions = a.get_permissions()
    size = a.get_filesize()

    return {
        "permissions": permissions,
        "apk_size": size
    }
