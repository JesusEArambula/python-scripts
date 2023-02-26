extensions = {
    "images": [".jpg", ".png", ".jpeg", ".gif", ".webp"],
    "videos": [".mp4", ".mkv"],
    "music": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP", ".java"],
    "design": [".xd", ".psd"]
}

dest = "C:\\Users\\swape\\OneDrive\\Documents\\Python Scripts\\Output Folder\\"
src = "C:\\Users\\swape\\OneDrive\\Documents\\Python Scripts\\Input Folder\\"
downloads = "C:\\Users\\swape\\Downloads\\"
desktop = "C:\\Users\\swape\\OneDrive\\Desktop\\"

def downloadingMsg():
    print("Downlading...")

def successMsg(file):
    msg = "\"" + file + "\"" + " has been downloaded successfully!"
    starMsg(msg, msgLength(msg))

def errorMsg(file):
    msg = "\"" + file + "\"" + " failed to download... :("
    dashLine(msg, msgLength(msg))

def starMsg(msg, length):
    starLine(length)
    print(msg)
    starLine(length)

def dashMsg(msg, length):
    dashLine(length)
    print(msg)
    dashLine(length)

def starLine(length):
    print("*" * length)

def dashLine(length):
    print("-" * length)

def msgLength(msg):
    return len(msg)