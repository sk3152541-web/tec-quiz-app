import json
import os
import shutil

# 1. Safety Backup
if os.path.exists("tec_questions.json"):
    shutil.copy("tec_questions.json", "tec_questions.json.bak")
    print("Safety Backup created successfully!")

data = {
    "modules": [
        {
            "module_id": 1,
            "module_name": "Digital Literacy & Computer Basics",
            "questions": [],
        },
        {
            "module_id": 2,
            "module_name": "CSC Services & Digital Schemes",
            "questions": [],
        },
        {
            "module_id": 3,
            "module_name": "Financial Literacy & Banking Services",
            "questions": [],
        },
        {
            "module_id": 4,
            "module_name": "Entrepreneurship & Business Management",
            "questions": [],
        },
    ]
}

# Module 1 ke liye 10 alag-alag parts (Har part mein 25 unique questions, Total = 250)
def generate_module_1_250():
    questions = []
    
    # 10 Categories / Parts ki master list (Har category ke concepts bilkul alag hain)
    parts_data = [
        # Part 1: Basic Computer & Hardware (Q1 - Q25)
        [
            ("Which of the following is known as the brain of the computer?", "Computer ka mukhya dimaag kise kaha jata hai?", "CPU (Central Processing Unit)", ["CPU (Central Processing Unit)", "RAM", "Hard Disk Drive", "Motherboard"]),
            ("What is the full form of CPU?", "CPU ka poora roop kya hota hai?", "Central Processing Unit", ["Central Processing Unit", "Computer Processing Utility", "Central Program Unit", "Control Processing User"]),
            ("Which part of the computer is considered its heart?", "Computer ka dil kise mana jata hai?", "Microprocessor / CPU", ["Microprocessor / CPU", "Monitor", "Keyboard", "Mouse"]),
            ("Which device is used to display output visually?", "Visual output dekhne ke liye kis device ka upyog hota hai?", "Monitor", ["Monitor", "Keyboard", "Printer", "Scanner"]),
            ("What type of device is a Computer Mouse?", "Computer mouse kis prakar ki device hai?", "Input Device", ["Input Device", "Output Device", "Storage Device", "Processing Device"]),
            ("What is the main function of a Power Supply (SMPS)?", "SMPS ka mukhya karya kya hai?", "To supply regulated power to computer components", ["To supply regulated power to computer components", "To store data permanently", "To connect to internet", "To print documents"]),
            ("Which component holds the chips that make up the computer's main memory?", "Computer ki main memory chips kahan lagi hoti hain?", "Motherboard", ["Motherboard", "Hard Disk", "Power Supply", "CD Drive"]),
            ("What is the full form of UPS?", "UPS ka poora roop kya hota hai?", "Uninterruptible Power Supply", ["Uninterruptible Power Supply", "Universal Power System", "Unified Power Source", "Utility Power Saver"]),
            ("What is the primary function of UPS?", "UPS ka mukhya upyog kisliye hota hai?", "To provide backup power during electricity failure", ["To provide backup power during electricity failure", "To increase internet speed", "To cool down the processor", "To format hard disk"]),
            ("Which device reads printed text or images and converts them into digital form?", "Printed text ko digital form mein badalne wali device kaun si hai?", "Scanner", ["Scanner", "Printer", "Speaker", "Monitor"]),
            ("Which printer uses tiny nozzles to spray ink onto paper?", "Paper par ink spray karne wale printer ko kya kehte hain?", "Inkjet Printer", ["Inkjet Printer", "Laser Printer", "Dot Matrix Printer", "Plotter"]),
            ("Which printer uses toner powder and laser technology?", "Laser technology aur toner powder ka upyog karne wala printer kaun sa hai?", "Laser Printer", ["Laser Printer", "Inkjet Printer", "Thermal Printer", "Impact Printer"]),
            ("Which of the following is an impact printer?", "Inmein se kaun sa ek impact printer hai?", "Dot Matrix Printer", ["Dot Matrix Printer", "Laser Printer", "Inkjet Printer", "3D Printer"]),
            ("What is a Joystick primarily used for?", "Joystick ka mukhya upyog kisliye hota hai?", "Playing video games", ["Playing video games", "Typing documents", "Printing files", "Scanning images"]),
            ("What is a Barcode Reader used for?", "Barcode reader ka upyog kiske liye hota hai?", "Reading product barcodes and pricing codes", ["Reading product barcodes and pricing codes", "Playing music", "Cleaning virus", "Creating spreadsheets"]),
            ("Which device is used for biometric attendance using fingerprints?", "Fingerprint se attendance lene wali device kaun si hai?", "Biometric Scanner", ["Biometric Scanner", "Webcam", "Projector", "Speaker"]),
            ("What is the use of a Microphone in a computer?", "Computer mein microphone ka kya upyog hota hai?", "To input audio or voice", ["To input audio or voice", "To output sound", "To display video", "To store data"]),
            ("What is the use of Speakers or Headphones?", "Speakers ya headphones ka kya karya hai?", "To output audio / sound", ["To output audio / sound", "To input voice", "To print text", "To scan documents"]),
            ("What is a Projector used for?", "Projector ka upyog kisliye hota hai?", "To display computer screen on a large wall or screen", ["To display computer screen on a large wall or screen", "To type fast", "To save files", "To transfer data"]),
            ("Which expansion card is used to connect a computer to a monitor?", "Monitor connect karne ke liye kis card ka upyog hota hai?", "Graphics Card / Video Card", ["Graphics Card / Video Card", "Sound Card", "Network Card", "Memory Card"]),
            ("What is the function of a Sound Card?", "Sound card ka mukhya karya kya hai?", "To process audio input and output", ["To process audio input and output", "To process graphics", "To manage internet", "To control power"]),
            ("Which port is used to connect high-definition monitors and TVs?", "HD monitors connect karne ke liye kis port ka upyog hota hai?", "HDMI Port", ["HDMI Port", "VGA Port", "Parallel Port", "Serial Port"]),
            ("What is a VGA port used for?", "VGA port ka upyog kisliye hota hai?", "To connect older monitors and display devices", ["To connect older monitors and display devices", "To connect internet cable", "To connect printer", "To plug USB drive"]),
            ("What is the physical equipment of a computer system called?", "Computer ke bhautik (physical) bhago ko kya kehte hain?", "Hardware", ["Hardware", "Software", "Firmware", "Malware"]),
            ("Which of the following is NOT hardware?", "Inmein se kaun sa hardware nahi hai?", "MS Word", ["Keyboard", "MS Word", "Monitor", "Hard Disk"])
        ],
        # Part 2: Memory & Storage Units (Q26 - Q50)
        [
            ("What is the smallest unit of data in a computer?", "Computer mein data ki sabse chhoti unit kaun si hai?", "Bit", ["Bit", "Byte", "Kilobyte", "Megabyte"]),
            ("How many bits make up one Byte?", "1 Byte kitne bits se milkar banta hai?", "8 Bits", ["4 Bits", "8 Bits", "16 Bits", "32 Bits"]),
            ("What does RAM stand for?", "RAM ka poora roop kya hota hai?", "Random Access Memory", ["Random Access Memory", "Readily Available Memory", "Run Active Memory", "Remote Access Module"]),
            ("What does ROM stand for?", "ROM ka poora roop kya hota hai?", "Read Only Memory", ["Read Only Memory", "Random Only Memory", "Readily Output Memory", "Run-time Operating Memory"]),
            ("Why is RAM called volatile memory?", "RAM ko volatile memory kyu kaha jata hai?", "Because it loses data when power is turned off", ["Because it loses data when power is turned off", "Because it is permanent", "Because it stores virus", "Because it is very slow"]),
            ("Why is ROM called non-volatile memory?", "ROM ko non-volatile memory kyu kehte hain?", "Because data remains safe even when power is off", ["Because data remains safe even when power is off", "Because data deletes automatically", "Because it works only on internet", "Because it is temporary"]),
            ("What is Cache Memory?", "Cache memory kya hoti hai?", "High-speed memory located close to CPU", ["High-speed memory located close to CPU", "A slow external hard drive", "A floppy disk", "A printer cable"]),
            ("1 Kilobyte (KB) is equal to how many bytes?", "1 Kilobyte (KB) kitne bytes ke barabar hota hai?", "1024 Bytes", ["1000 Bytes", "1024 Bytes", "512 Bytes", "2048 Bytes"]),
            ("1 Megabyte (MB) is equal to how many KBs?", "1 Megabyte (MB) kitne KB ke barabar hota hai?", "1024 KB", ["1000 KB", "1024 KB", "512 KB", "2048 KB"]),
            ("1 Gigabyte (GB) is equal to how many MBs?", "1 Gigabyte (GB) kitne MB ke barabar hota hai?", "1024 MB", ["1000 MB", "1024 MB", "2048 MB", "512 MB"]),
            ("1 Terabyte (TB) is equal to how many GBs?", "1 Terabyte (TB) kitne GB ke barabar hota hai?", "1024 GB", ["1000 GB", "1024 GB", "500 GB", "2048 GB"]),
            ("Which storage device uses magnetic disks to store large amounts of data?", "Magnetic disk ka upyog karke bada data kismein store hota hai?", "Hard Disk Drive (HDD)", ["Hard Disk Drive (HDD)", "CD-ROM", "RAM", "Cache"]),
            ("What is Solid State Drive (SSD)?", "Solid State Drive (SSD) kya hai?", "A fast storage device using flash memory", ["A fast storage device using flash memory", "An old magnetic tape", "A printer type", "A display screen"]),
            ("Which storage medium is optical in nature?", "Inmein se kaun sa optical storage medium hai?", "CD / DVD / Blu-ray Disc", ["CD / DVD / Blu-ray Disc", "Hard Disk", "RAM", "Floppy Disk"]),
            ("What is the storage capacity of a standard CD-ROM?", "Ek standard CD-ROM ki storage capacity kitni hoti hai?", "700 MB", ["700 MB", "4.7 GB", "25 GB", "1.44 MB"]),
            ("What is the storage capacity of a standard DVD-ROM?", "Ek standard DVD-ROM ki capacity kitni hoti hai?", "4.7 GB", ["700 MB", "4.7 GB", "50 GB", "700 KB"]),
            ("What is the storage capacity of a single-layer Blu-ray disc?", "Single-layer Blu-ray disc ki capacity kitni hoti hai?", "25 GB", ["4.7 GB", "25 GB", "700 MB", "700 GB"]),
            ("What was the capacity of a traditional Floppy Disk?", "Purane floppy disk ki capacity kitni hoti thi?", "1.44 MB", ["1.44 MB", "700 MB", "4.7 GB", "10 GB"]),
            ("What is a Pen Drive / USB Flash Drive used for?", "Pen drive ka mukhya upyog kisliye hota hai?", "Portable data storage and transfer", ["Portable data storage and transfer", "To clean computer viruses", "To print bills", "To connect to LAN"]),
            ("What is Virtual Memory?", "Virtual Memory kya hoti hai?", "Memory created using hard disk space when RAM is full", ["Memory created using hard disk space when RAM is full", "Permanent ROM chip", "External hard drive", "Cache memory inside CPU"]),
            ("What is EEPROM?", "EEPROM ka poora roop kya hai?", "Electrically Erasable Programmable Read-Only Memory", ["Electrically Erasable Programmable Read-Only Memory", "External Electronic Program Read-Only Memory", "Easy Electrical Power ROM", "Extended Engine Processing RAM"]),
            ("What is PROM?", "PROM ka poora roop kya hota hai?", "Programmable Read-Only Memory", ["Programmable Read-Only Memory", "Primary Read-Only Media", "Process RAM Output Memory", "Permanent Routine Operating Module"]),
            ("Which memory is directly accessed by the CPU?", "CPU dwara sabse pehle aur seedhe kis memory ko access kiya jata hai?", "Primary Memory (RAM / Cache)", ["Primary Memory (RAM / Cache)", "Hard Disk", "Pen Drive", "CD-ROM"]),
            ("Which of the following is secondary memory?", "Inmein se kaun si secondary memory hai?", "Hard Disk Drive", ["RAM", "Cache", "Registers", "ROM"]),
            ("What is the main advantage of SSD over HDD?", "HDD ki tulna mein SSD ka mukhya labh kya hai?", "Much faster read/write speed and no moving parts", ["Much faster read/write speed and no moving parts", "Cheaper price", "Larger physical size", "Consumes more power"])
        ],
        # Part 3: Operating Systems & Software (Q51 - Q75)
        [
            ("What is an Operating System (OS)?", "Operating System (OS) kya hota hai?", "System software that acts as an interface between user and hardware", ["System software that acts as an interface between user and hardware", "An antivirus program", "A word processor", "An internet browser"]),
            ("Which of the following is an Operating System?", "Inmein se kaun sa ek Operating System hai?", "Microsoft Windows", ["Microsoft Windows", "MS Word", "Google Chrome", "Adobe Photoshop"]),
            ("Which company developed the Windows Operating System?", "Windows Operating System kis company ne banaya hai?", "Microsoft", ["Microsoft", "Apple", "Google", "IBM"]),
            ("Which of the following is an open-source mobile Operating System?", "Inmein se kaun sa open-source mobile OS hai?", "Android", ["Android", "iOS", "Windows Phone", "MS DOS"]),
            ("Which Operating System is developed by Apple for iPhones?", "Apple dwara iPhone ke liye banaya gaya OS kaun sa hai?", "iOS", ["iOS", "Android", "Linux", "Windows"]),
            ("What is Linux?", "Linux kya hai?", "An open-source Unix-like Operating System", ["An open-source Unix-like Operating System", "A computer virus", "A text editor", "A web browser"]),
            ("What is the core component of an Operating System?", "Operating System ka mukhya core component kya kehlata hai?", "Kernel", ["Kernel", "Shell", "Driver", "Application"]),
            ("What is a Device Driver?", "Device Driver kya hota hai?", "Software that allows OS to communicate with hardware devices", ["Software that allows OS to communicate with hardware devices", "An antivirus tool", "A game controller", "A database file"]),
            ("What is multitasking in an Operating System?", "Multitasking ka kya arth hai?", "Running multiple applications simultaneously", ["Running multiple applications simultaneously", "Running only one program", "Shutting down system", "Deleting files"]),
            ("What is Booting?", "Booting process kya hoti hai?", "Starting up the computer and loading OS into RAM", ["Starting up the computer and loading OS into RAM", "Turning off the computer", "Formatting hard disk", "Installing antivirus"]),
            ("What is Cold Booting?", "Cold Booting kise kehte hain?", "Starting a computer from completely powered-off state", ["Starting a computer from completely powered-off state", "Restarting a running computer", "Putting PC to sleep", "Logging off user"]),
            ("What is Warm Booting?", "Warm Booting kise kehte hain?", "Restarting a computer that is already powered on", ["Restarting a computer that is already powered on", "Starting after 2 hours", "Turning on power switch", "Unplugging main wire"]),
            ("What is GUI in computing?", "Computing mein GUI ka poora roop kya hai?", "Graphical User Interface", ["Graphical User Interface", "General User Interaction", "Global Utility Integration", "Great Unified Internet"]),
            ("What is CLI?", "CLI ka poora roop kya hota hai?", "Command Line Interface", ["Command Line Interface", "Computer Local Input", "Common Language Instruction", "Core Logic Integration"]),
            ("Which of the following is an example of System Software?", "Inmein se kaun sa System Software ka udaharan hai?", "Operating System", ["Operating System", "MS Word", "VLC Media Player", "Adobe Photoshop"]),
            ("Which of the following is Application Software?", "Inmein se kaun sa Application Software hai?", "MS Excel", ["MS Excel", "Windows OS", "Linux", "BIOS"]),
            ("What is Utility Software?", "Utility Software ka kya karya hota hai?", "Software designed to maintain and configure computer systems", ["Software designed to maintain and configure computer systems", "To play 3D games", "To create presentations", "To browse websites"]),
            ("Which of the following is a utility software?", "Inmein se kaun sa utility software hai?", "Antivirus / Disk Defragmenter", ["Antivirus / Disk Defragmenter", "MS Word", "Google Chrome", "Windows OS"]),
            ("What is Open Source Software?", "Open Source Software kya hota hai?", "Software whose source code is freely available to public", ["Software whose source code is freely available to public", "Software that costs very high money", "Software that cannot be modified", "Software made only for Government"]),
            ("What is Proprietary Software?", "Proprietary Software kya hota hai?", "Software whose source code is legally protected and not freely public", ["Software whose source code is legally protected and not freely public", "Free software for everyone", "Open source linux", "Public domain tool"]),
            ("What is Firmware?", "Firmware kya hota hai?", "Permanent software programmed into a hardware device ROM", ["Permanent software programmed into a hardware device ROM", "Temporary RAM data", "An online browser", "A mobile game"]),
            ("What is the function of Disk Defragmenter?", "Disk Defragmenter ka kya karya hota hai?", "To rearrange fragmented data and improve disk performance", ["To rearrange fragmented data and improve disk performance", "To delete all files", "To install Windows", "To scan viruses"]),
            ("What is the function of a File Manager?", "File Manager ka mukhya upyog kya hai?", "To organize, create, and manage files and folders", ["To organize, create, and manage files and folders", "To send emails", "To play music", "To edit photos"]),
            ("What is a Task Manager used for in Windows?", "Task Manager ka upyog kisliye hota hai?", "To view and manage running applications and system performance", ["To view and manage running applications and system performance", "To clean dust from keyboard", "To change desktop wallpaper", "To install new drivers"]),
            ("What is Shareware?", "Shareware kya hota hai?", "Software distributed freely on trial basis before purchase", ["Software distributed freely on trial basis before purchase", "Totally free software forever", "Pirated software", "Hardware tool"])
        ],
        # Part 4: MS Word & Word Processing (Q76 - Q100)
        [
            ("What type of software is MS Word?", "MS Word kis prakar ka software hai?", "Word Processor", ["Word Processor", "Spreadsheet", "Database", "Presentation"]),
            ("What is the default file extension of MS Word documents (2007 and later)?", "MS Word files ka default extension kya hota hai?", ".docx", [".docx", ".doc", ".xls", ".ppt"]),
            ("What is the default file extension of older MS Word documents (2003)?", "Purane MS Word (2003) ka extension kya tha?", ".doc", [".doc", ".docx", ".xls", ".txt"]),
            ("Which shortcut key is used to Save a document in MS Word?", "Document ko save karne ki shortcut key kya hai?", "Ctrl + S", ["Ctrl + S", "Ctrl + C", "Ctrl + P", "Ctrl + V"]),
            ("What is the shortcut key to Open an existing document?", "Pehle se bani file ko kholne ki shortcut key kya hai?", "Ctrl + O", ["Ctrl + O", "Ctrl + N", "Ctrl + S", "Ctrl + W"]),
            ("What is the shortcut key to create a New document?", "Naya document banane ki shortcut key kya hai?", "Ctrl + N", ["Ctrl + N", "Ctrl + O", "Ctrl + M", "Ctrl + D"]),
            ("What is the shortcut key to Print a document?", "Document print karne ke liye kaun si shortcut key hai?", "Ctrl + P", ["Ctrl + P", "Ctrl + T", "Ctrl + R", "Ctrl + Shift + P"]),
            ("What is the shortcut key for Undo in MS Word?", "Undo karne ke liye kaun si shortcut key hai?", "Ctrl + Z", ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + A"]),
            ("What is the shortcut key for Redo in MS Word?", "Redo karne ke liye kaun si shortcut key hai?", "Ctrl + Y", ["Ctrl + Y", "Ctrl + Z", "Ctrl + R", "Ctrl + D"]),
            ("What shortcut key is used to Select All text in a document?", "Poora text select karne ki shortcut key kya hai?", "Ctrl + A", ["Ctrl + A", "Ctrl + S", "Ctrl + F", "Ctrl + B"]),
            ("What shortcut key is used to Bold selected text?", "Text ko Bold karne ki shortcut key kya hai?", "Ctrl + B", ["Ctrl + B", "Ctrl + I", "Ctrl + U", "Ctrl + D"]),
            ("What shortcut key is used to Italicize selected text?", "Text ko Italic karne ki shortcut key kya hai?", "Ctrl + I", ["Ctrl + I", "Ctrl + B", "Ctrl + U", "Ctrl + T"]),
            ("What shortcut key is used to Underline selected text?", "Text ke niche line (Underline) laane ki shortcut key kya hai?", "Ctrl + U", ["Ctrl + U", "Ctrl + L", "Ctrl + N", "Ctrl + K"]),
            ("What is the shortcut key to Find text in a document?", "Document mein text dhoondne (Find) ki shortcut key kya hai?", "Ctrl + F", ["Ctrl + F", "Ctrl + H", "Ctrl + G", "Ctrl + P"]),
            ("What is the shortcut key for Replace feature in MS Word?", "Replace feature ki shortcut key kya hai?", "Ctrl + H", ["Ctrl + H", "Ctrl + F", "Ctrl + R", "Ctrl + E"]),
            ("What is the shortcut key to Align text to the Center?", "Text ko Center align karne ki shortcut key kya hai?", "Ctrl + E", ["Ctrl + E", "Ctrl + L", "Ctrl + R", "Ctrl + J"]),
            ("What is the shortcut key for Left Alignment?", "Left alignment ki shortcut key kya hai?", "Ctrl + L", ["Ctrl + L", "Ctrl + E", "Ctrl + R", "Ctrl + J"]),
            ("What is the shortcut key for Right Alignment?", "Right alignment ki shortcut key kya hai?", "Ctrl + R", ["Ctrl + R", "Ctrl + L", "Ctrl + E", "Ctrl + J"]),
            ("What is the shortcut key for Justify Alignment?", "Justify alignment ki shortcut key kya hai?", "Ctrl + J", ["Ctrl + J", "Ctrl + L", "Ctrl + E", "Ctrl + R"]),
            ("What is the purpose of Spell Check in MS Word?", "Spell Check ka kya upyog hai?", "To check and correct spelling and grammar errors", ["To check and correct spelling and grammar errors", "To check internet speed", "To design graphics", "To print pages"]),
            ("Which function key is used to run Spell Check in MS Word?", "Spell Check run karne ke liye kis Function key ka upyog hota hai?", "F7", ["F7", "F5", "F2", "F12"]),
            ("What is Mail Merge in MS Word?", "Mail Merge ka kya upyog hai?", "To send personalized letters and documents to multiple recipients", ["To send personalized letters and documents to multiple recipients", "To merge two doc files into one", "To send emails via Outlook", "To check spelling"]),
            ("What is the maximum zoom percentage available in MS Word?", "MS Word mein maximum zoom kitna ho sakta hai?", "500%", ["500%", "100%", "200%", "1000%"]),
            ("What is a Hyperlink in MS Word?", "Hyperlink ka kya karya hai?", "To create a link to a webpage, file, or email address", ["To create a link to a webpage, file, or email address", "To highlight text in yellow", "To insert a table", "To check spelling"]),
            ("What is a Watermark in MS Word?", "Watermark ka kya upyog hai?", "Faint background text or image behind document text", ["Faint background text or image behind document text", "A digital signature", "Page border line", "Header and footer"])
        ],
        # Part 5: MS Excel & Spreadsheets (Q101 - Q125)
        [
            ("What type of software is MS Excel?", "MS Excel kis prakar ka software hai?", "Spreadsheet Software", ["Spreadsheet Software", "Word Processor", "Presentation Tool", "Database Manager"]),
            ("What is the default file extension of MS Excel files (2007 and later)?", "MS Excel files ka default extension kya hota hai?", ".xlsx", [".xlsx", ".docx", ".pptx", ".txt"]),
            ("What is the intersection of a row and a column in Excel called?", "Row aur column ke milne wale box ko kya kehte hain?", "Cell", ["Cell", "Grid", "Table", "Sheet"]),
            ("How are columns labeled in MS Excel?", "MS Excel mein columns ko kaise label kiya jata hai?", "Letters (A, B, C... AA, AB)", ["Letters (A, B, C... AA, AB)", "Numbers (1, 2, 3...)", "Roman Numerals (I, II, III)", "Symbols (!, @, #)"]),
            ("How are rows labeled in MS Excel?", "MS Excel mein rows ko kaise label kiya jata hai?", "Numbers (1, 2, 3...)", ["Numbers (1, 2, 3...)", "Letters (A, B, C...)", "Names", "Colors"]),
            ("What symbol must every formula in Excel begin with?", "Excel ka har formula kis symbol se shuru hona chahiye?", "=", ["=", "+", "-", "*"]),
            ("Which function in Excel is used to calculate the sum of a range of cells?", "Cells ka total nikalne ke liye kis function ka upyog hota hai?", "SUM", ["SUM", "TOTAL", "ADD", "PLUS"]),
            ("Which function is used to find the average value in Excel?", "Average nikalne ke liye kaun sa function hai?", "AVERAGE", ["AVERAGE", "MEAN", "MEDIAN", "SUM"]),
            ("Which function finds the highest value in a range?", "Sabse badi value nikalne ke liye kaun sa function hai?", "MAX", ["MAX", "HIGH", "TOP", "LARGE"]),
            ("Which function finds the lowest value in a range?", "Sabse choti value nikalne ke liye kaun sa function hai?", "MIN", ["MIN", "LOW", "SMALL", "BOTTOM"]),
            ("Which function counts the number of cells containing numbers?", "Numbers wale cells ko count karne ke liye kaun sa function hai?", "COUNT", ["COUNT", "COUNTA", "SUM", "NUMBER"]),
            ("What is the shortcut key to insert a new current date in Excel?", "Current date insert karne ki shortcut key kya hai?", "Ctrl + ;", ["Ctrl + ;", "Ctrl + Shift + ;", "Ctrl + D", "Ctrl + T"]),
            ("What does the error value '###' mean in an Excel cell?", "Excel cell mein '###' error ka kya matlab hai?", "Column is too narrow to display the content", ["Column is too narrow to display the content", "Formula is wrong", "Division by zero", "File is deleted"]),
            ("What does '#DIV/0!' error mean in Excel?", "'#DIV/0!' error ka kya arth hai?", "Formula is dividing a number by zero", ["Formula is dividing a number by zero", "Cell is empty", "Invalid function name", "Wrong text format"]),
            ("What is an active cell in Excel?", "Active cell kise kehte hain?", "The currently selected cell with a dark border", ["The currently selected cell with a dark border", "The last cell in sheet", "A locked cell", "A printed cell"]),
            ("What is a Workbook in MS Excel?", "MS Excel mein Workbook kya hoti hai?", "A collection of multiple worksheets", ["A collection of multiple worksheets", "A single text page", "A chart design", "An antivirus scan"]),
            ("What is the shortcut key to create a new Chart in Excel?", "Chart banane ki shortcut key kya hai?", "F11", ["F11", "F5", "F2", "Ctrl + C"]),
            ("What is conditional formatting used for in Excel?", "Conditional formatting ka upyog kisliye hota hai?", "To highlight cells based on specific rules or values", ["To highlight cells based on specific rules or values", "To print pages", "To lock password", "To save file"]),
            ("What is a Pivot Table used for?", "Pivot Table ka mukhya upyog kya hai?", "To summarize, analyze, and manipulate large amounts of data", ["To summarize, analyze, and manipulate large amounts of data", "To create a chart", "To check spelling", "To send emails"]),
            ("What does VLOOKUP stand for in Excel?", "VLOOKUP ka poora roop kya hai?", "Vertical Lookup", ["Vertical Lookup", "Value Lookup", "Visual Link Utility", "Variable Local Operation"]),
            ("What is the function of VLOOKUP?", "VLOOKUP function ka kya karya hai?", "To search for a value in the leftmost column of a table", ["To search for a value in the leftmost column of a table", "To add numbers vertically", "To sort data alphabetically", "To count blank cells"]),
            ("Which feature is used to arrange rows in ascending or descending order?", "Data ko alphabetical order mein lagane ke liye kiska upyog hota hai?", "Sort", ["Sort", "Filter", "Merge", "Pivot"]),
            ("Which feature is used to temporarily hide rows that do not meet criteria?", "Kuch rows ko temporarily chupane ke liye kiska upyog hota hai?", "Filter", ["Filter", "Sort", "Lock", "Protect"]),
            ("What is the shortcut key to open the Format Cells dialog box?", "Format Cells dialog box kholne ki shortcut key kya hai?", "Ctrl + 1", ["Ctrl + 1", "Ctrl + F", "Ctrl + Shift + F", "Ctrl + C"]),
            ("What is the extension of Excel macro-enabled workbook?", "Macro-enabled Excel workbook ka extension kya hota hai?", ".xlsm", [".xlsm", ".xlsx", ".xls", ".docm"])
        ],
        # Part 6: PowerPoint & Presentations (Q126 - Q150)
        [
            ("What type of software is MS PowerPoint?", "MS PowerPoint kis prakar ka software hai?", "Presentation Software", ["Presentation Software", "Spreadsheet", "Word Processor", "Database"]),
            ("What is the default file extension of PowerPoint presentations?", "PowerPoint files ka default extension kya hota hai?", ".pptx", [".pptx", ".docx", ".xlsx", ".txt"]),
            ("What is an individual page in a PowerPoint presentation called?", "PowerPoint ke ek page ko kya kehte hain?", "Slide", ["Slide", "Page", "Sheet", "Document"]),
            ("What is the shortcut key to start a slideshow from the beginning?", "Shuru se slideshow start karne ki shortcut key kya hai?", "F5", ["F5", "F1", "F10", "F12"]),
            ("What is the shortcut key to start slideshow from the current slide?", "Current slide se slideshow start karne ki shortcut key kya hai?", "Shift + F5", ["Shift + F5", "Ctrl + F5", "Alt + F5", "F5"]),
            ("What is a Slide Master used for?", "Slide Master ka mukhya upyog kya hai?", "To control the global design and formatting of all slides", ["To control the global design and formatting of all slides", "To play background music", "To print pages", "To delete slides"]),
            ("What are custom animations in PowerPoint?", "Custom animations kya hoti hain?", "Visual effects applied to elements on a slide", ["Visual effects applied to elements on a slide", "Transition between slides", "Sound effects for errors", "Printer settings"]),
            ("What are slide transitions?", "Slide transitions kya hoti hain?", "Visual special effects when moving from one slide to another", ["Visual special effects when moving from one slide to another", "Animations inside text", "Background colors", "Saving files"]),
            ("What is the shortcut key to insert a new slide in PowerPoint?", "Nayi slide insert karne ki shortcut key kya hai?", "Ctrl + M", ["Ctrl + M", "Ctrl + N", "Ctrl + S", "Ctrl + P"]),
            ("Which view displays thumbnail images of all slides together?", "Sabhi slides ke thumbnails ek sath dekhne ke liye kaun sa view hota hai?", "Slide Sorter View", ["Slide Sorter View", "Normal View", "Reading View", "Master View"]),
            ("Can we insert videos and audio clips in PowerPoint presentations?", "Kya hum PowerPoint mein video aur audio daal sakte hain?", "Yes, multimedia files can be inserted", ["Yes, multimedia files can be inserted", "No, only text is allowed", "Only images are allowed", "Only in PDF format"]),
            ("What is the purpose of the 'Rehearse Timings' feature?", "Rehearse Timings feature ka upyog kisliye hota hai?", "To record and practice the time spent on each slide", ["To record and practice the time spent on each slide", "To check spelling", "To print slides", "To change font size"]),
            ("What is the shortcut key to duplicate the selected slide?", "Selected slide ki duplicate copy banane ki shortcut key kya hai?", "Ctrl + D", ["Ctrl + D", "Ctrl + C", "Ctrl + V", "Ctrl + P"]),
            ("What is the default slide orientation in PowerPoint?", "PowerPoint mein default slide orientation kya hoti hai?", "Landscape", ["Landscape", "Portrait", "Square", "Vertical"]),
            ("Which file format can be used to save a PowerPoint presentation as a video?", "Presentation ko video ke roop mein save karne ke liye kaun sa format hai?", ".mp4 or .wmv", [".mp4 or .wmv", ".docx", ".xlsx", ".txt"]),
            ("What is the shortcut key to end a slideshow presentation?", "Slideshow ko beech mein rokne ya band karne ke liye kaun si key dabate hain?", "Esc", ["Esc", "F5", "Enter", "Spacebar"]),
            ("What is the purpose of adding speaker notes?", "Speaker notes ka kya upyog hota hai?", "Notes for the presenter that are hidden from the audience", ["Notes for the presenter that are hidden from the audience", "Subtitles for video", "Background music", "Slide numbering"]),
            ("What is SmartArt used for in PowerPoint?", "SmartArt ka upyog kisliye hota hai?", "To create diagrams, flowcharts, and visual graphics", ["To create diagrams, flowcharts, and visual graphics", "To check spellings", "To play animations", "To calculate numbers"]),
            ("Can we apply a password to protect a PowerPoint presentation?", "Kya hum PowerPoint presentation par password laga sakte hain?", "Yes, presentations can be encrypted with a password", ["Yes, presentations can be encrypted with a password", "No, security is not supported", "Only in MS Word", "Only on Mac"]),
            ("What is the extension of a PowerPoint template file?", "PowerPoint template file ka extension kya hota hai?", ".potx", [".potx", ".pptx", ".ppsx", ".txt"]),
            ("What is a PowerPoint Show file extension?", "PowerPoint Show file ka extension kya hota hai jo direct open hoti hai?", ".ppsx", [".ppsx", ".pptx", ".potx", ".docx"]),
            ("How can you hide a specific slide during a slideshow without deleting it?", "Bina delete kiye kisi slide ko slideshow se hide kaise karein?", "Right click slide and select Hide Slide", ["Right click slide and select Hide Slide", "Press Delete key", "Cut the slide", "Lock the file"]),
            ("What is the maximum zoom level in PowerPoint?", "PowerPoint mein maximum zoom kitna ho sakta hai?", "400%", ["400%", "100%", "200%", "500%"]),
            ("What is an Action Button in PowerPoint?", "Action Button ka kya karya hota hai?", "A clickable button that links to another slide, URL, or program", ["A clickable button that links to another slide, URL, or program", "A print button", "A spelling checker", "A font style"]),
            ("Which menu tab contains commands to apply slide transitions?", "Slide transitions lagane ke liye kis menu tab par jana padta hai?", "Transitions", ["Transitions", "Animations", "Design", "Home"])
        ],
        # Part 7: Internet, WWW & Web Browsers (Q151 - Q175)
        [
            ("What does WWW stand for?", "WWW ka poora roop kya hota hai?", "World Wide Web", ["World Wide Web", "World Web Wide", "Wide World Web", "Web World Wide"]),
            ("Who is known as the inventor of the World Wide Web?", "World Wide Web (WWW) ke aavishkarak kise mana jata hai?", "Tim Berners-Lee", ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Alan Turing"]),
            ("What is a Web Browser?", "Web browser kya hota hai?", "An application software used to access and view websites", ["An application software used to access and view websites", "A computer hardware device", "An antivirus program", "A database server"]),
            ("Which of the following is a popular Web Browser?", "Inmein se kaun sa ek lokpriya web browser hai?", "Google Chrome", ["Google Chrome", "MS Word", "Notepad", "Windows Media Player"]),
            ("What is a Search Engine?", "Search engine kya hota hai?", "A website used to search for information on the internet", ["A website used to search for information on the internet", "An email client", "A computer virus", "A printer driver"]),
            ("Which of the following is a well-known Search Engine?", "Inmein se kaun sa ek famous search engine hai?", "Google", ["Google", "Microsoft Word", "Adobe", "Windows"]),
            ("What does URL stand for?", "URL ka poora roop kya hota hai?", "Uniform Resource Locator", ["Uniform Resource Locator", "Universal Record Link", "Unified Retrieval Logic", "User Remote Line"]),
            ("What is an IP Address?", "IP Address kya hota hai?", "A unique numerical address assigned to every device on a network", ["A unique numerical address assigned to every device on a network", "A password for email", "A hardware serial number", "A browser name"]),
            ("What does HTTP stand for in website addresses?", "HTTP ka poora roop kya hota hai?", "HyperText Transfer Protocol", ["HyperText Transfer Protocol", "HyperText Transmission Process", "High Transfer Text Protocol", "Hyperlink Transfer Program"]),
            ("Why is HTTPS more secure than HTTP?", "HTTPS, HTTP se zyada surakshit kyu hota hai?", "Because it uses encryption (SSL/TLS) for secure data transfer", ["Because it uses encryption (SSL/TLS) for secure data transfer", "Because it is faster", "Because it is free", "Because it requires no internet"]),
            ("What is an ISP?", "ISP ka poora roop kya hota hai?", "Internet Service Provider", ["Internet Service Provider", "Internal System Protocol", "International Software Program", "Information Security Policy"]),
            ("What is Email?", "Email ka poora roop kya hota hai?", "Electronic Mail", ["Electronic Mail", "Electrical Message", "Easy Mail Link", "Express Message App"]),
            ("Who is considered the father of Email?", "Email ke janak (father) kise kaha jata hai?", "Ray Tomlinson", ["Ray Tomlinson", "Tim Berners-Lee", "Vint Cerf", "Mark Zuckerberg"]),
            ("What is the '@' symbol used for in email addresses?", "Email address mein '@' symbol ka kya upyog hai?", "To separate username from domain name", ["To separate username from domain name", "To encrypt password", "To attach files", "To send speed message"]),
            ("What is Spam in email terminology?", "Email mein Spam kya hota hai?", "Unsolicited bulk or junk commercial emails", ["Unsolicited bulk or junk commercial emails", "Important official messages", "Deleted drafts", "Secure incoming mail"]),
            ("What is the function of CC in an email?", "Email mein CC (Carbon Copy) ka kya upyog hai?", "To send a copy of the email to other recipients visibly", ["To send a copy of the email to other recipients visibly", "To hide recipient email", "To delete mail", "To block user"]),
            ("What is the function of BCC in an email?", "Email mein BCC (Blind Carbon Copy) ka kya upyog hai?", "To send a copy secretly without other recipients knowing", ["To send a copy secretly without other recipients knowing", "To attach a big file", "To reply automatically", "To encrypt text"]),
            ("What is a Web Page?", "Web page kya hota hai?", "A document on the World Wide Web written in HTML", ["A document on the World Wide Web written in HTML", "A printed book page", "An MS Word file", "An Excel sheet"]),
            ("What is a Website?", "Website kya hoti hai?", "A collection of related web pages under a single domain name", ["A collection of related web pages under a single domain name", "A single text file", "A video player", "An offline game"]),
            ("What is HTML?", "HTML ka poora roop kya hota hai?", "HyperText Markup Language", ["HyperText Markup Language", "High Tech Modern Language", "Hyperlink Transfer Markup Link", "Home Tool Multi Language"]),
            ("What is a Domain Name?", "Domain name kya hota hai?", "Human-readable address of a website (e.g., google.com)", ["Human-readable address of a website (e.g., google.com)", "Numerical IP address", "Computer password", "Email login ID"]),
            ("What does DNS stand for on the internet?", "DNS ka poora roop kya hota hai?", "Domain Name System", ["Domain Name System", "Digital Network Service", "Data Name Server", "Direct Network System"]),
            ("What is the function of DNS?", "DNS ka mukhya karya kya hai?", "To translate domain names into IP addresses", ["To translate domain names into IP addresses", "To block viruses", "To send emails", "To design web pages"]),
            ("What is a Cookie in web browsing?", "Web browsing mein Cookie kya hoti hai?", "Small data stored by website on user's browser for session tracking", ["Small data stored by website on user's browser for session tracking", "A computer virus", "An internet cable", "A security password"]),
            ("What is Cloud Computing?", "Cloud Computing kya hoti hai?", "Storing and accessing data and programs over the internet instead of computer hard drive", ["Storing and accessing data and programs over the internet instead of computer hard drive", "Gaming on local PC", "Printing documents online", "Scanning computer for viruses"])
        ],
        # Part 8: Networking & Communication (Q176 - Q200)
        [
            ("What is a Computer Network?", "Computer network kya hota hai?", "Interconnection of two or more computers to share resources", ["Interconnection of two or more computers to share resources", "A single standalone PC", "A printer connected to power", "An offline game setup"]),
            ("What does LAN stand for?", "LAN ka poora roop kya hota hai?", "Local Area Network", ["Local Area Network", "Large Area Node", "Local Access Net", "Light Application Network"]),
            ("What does WAN stand for?", "WAN ka poora roop kya hota hai?", "Wide Area Network", ["Wide Area Network", "Web Access Node", "Wireless Area Network", "Width Application Net"]),
            ("What does MAN stand for?", "MAN ka poora roop kya hota hai?", "Metropolitan Area Network", ["Metropolitan Area Network", "Mega Access Network", "Main Area Node", "Mobile Application Network"]),
            ("What is a PAN (Personal Area Network)?", "PAN network ka daayra kitna hota hai?", "Network centered around a single person within a range of 10 meters", ["Network centered around a single person within a range of 10 meters", "Spanning across a whole country", "Connecting multiple cities", "Connecting global servers"]),
            ("What is a Router in networking?", "Networking mein Router ka kya karya hai?", "To forward data packets between different computer networks", ["To forward data packets between different computer networks", "To print documents", "To store permanent backups", "To scan viruses"]),
            ("What is a Switch in a network?", "Network mein Switch ka kya upyog hota hai?", "To connect devices together on a computer network using packet switching", ["To connect devices together on a computer network using packet switching", "To convert analog signals", "To block internet", "To supply electricity"]),
            ("What is a Modem used for?", "Modem ka mukhya upyog kisliye hota hai?", "To modulate and demodulate signals between digital devices and telephone lines", ["To modulate and demodulate signals between digital devices and telephone lines", "To print papers", "To scan documents", "To cool CPU"]),
            ("What is Wi-Fi?", "Wi-Fi kya hoti hai?", "Wireless local area networking technology", ["Wireless local area networking technology", "A wired cable connection", "A computer virus", "A brand of hard disk"]),
            ("What does Wi-Fi stand for?", "Wi-Fi ka official full form kya hai?", "Wireless Fidelity (trademark term)", ["Wireless Fidelity (trademark term)", "Wireless Finder", "Wide Frequency Internet", "Web File Integration"]),
            ("What is Bluetooth?", "Bluetooth kya hai?", "Wireless technology for exchanging data over short distances", ["Wireless technology for exchanging data over short distances", "A long-range satellite network", "A high-speed printer cable", "An operating system"]),
            ("What is Ethernet?", "Ethernet kya hoti hai?", "A traditional technology for connecting wired local area networks (LAN)", ["A traditional technology for connecting wired local area networks (LAN)", "A wireless mouse", "An email protocol", "A web browser"]),
            ("What is an Ethernet Cable (RJ45)?", "RJ45 Ethernet cable ka upyog kisliye hota hai?", "To connect computers to a wired network or router", ["To connect computers to a wired network or router", "To connect monitor to CPU", "To plug power cord", "To connect USB mouse"]),
            ("What is a Network Topology?", "Network Topology kya hoti hai?", "The arrangement of various elements of a computer network", ["The arrangement of various elements of a computer network", "Speed of internet", "Type of web browser", "Size of computer screen"]),
            ("Which network topology has devices connected in a circular loop?", "Kis network topology mein devices ek gol ring mein jude hote hain?", "Ring Topology", ["Ring Topology", "Star Topology", "Bus Topology", "Mesh Topology"]),
            ("In which topology is every device connected to a central hub or switch?", "Kis topology mein sabhi devices ek central switch ya hub se jude hote hain?", "Star Topology", ["Star Topology", "Ring Topology", "Bus Topology", "Tree Topology"]),
            ("What is Bus Topology?", "Bus Topology mein devices kaise jude hote hain?", "All devices connected to a single central cable (backbone)", ["All devices connected to a single central cable (backbone)", "In a circular ring", "Directly to each other", "In a hierarchical tree"]),
            ("What is Mesh Topology?", "Mesh Topology ki kya visheshta hai?", "Every device has a dedicated point-to-point link to every other device", ["Every device has a dedicated point-to-point link to every other device", "Single cable connection", "Ring structure", "Central hub only"]),
            ("What is an IP address version 4 (IPv4) length?", "IPv4 address kitne bits ka hota hai?", "32 bits", ["32 bits", "64 bits", "128 bits", "16 bits"]),
            ("What is an IP address version 6 (IPv6) length?", "IPv6 address kitne bits ka hota hai?", "128 bits", ["32 bits", "64 bits", "128 bits", "256 bits"]),
            ("What is a MAC Address?", "MAC Address kya hota hai?", "Hardware identification number unique to each network adapter", ["Hardware identification number unique to each network adapter", "Temporary IP address", "User email password", "Website domain name"]),
            ("What is FTP?", "FTP ka poora roop kya hota hai?", "File Transfer Protocol", ["File Transfer Protocol", "Fast Text Process", "File Transmission Program", "Folder Transfer Path"]),
            ("What is the primary use of FTP?", "FTP ka mukhya upyog kisliye hota hai?", "To transfer files between a client and server over a network", ["To transfer files between a client and server over a network", "To send instant text messages", "To browse web pages", "To scan malware"]),
            ("What is TCP/IP?", "TCP/IP ka poora roop kya hai?", "Transmission Control Protocol / Internet Protocol", ["Transmission Control Protocol / Internet Protocol", "Transfer Computer Program / IP", "Total Connection Process / Internet", "Technical Communication Port"]),
            ("What is a Gateway in networking?", "Networking mein Gateway kya hota hai?", "A node that connects two different networks using different protocols", ["A node that connects two different networks using different protocols", "A simple mouse pad", "A power plug", "A computer screen"])
        ],
        # Part 9: Cyber Security & Computer Threats (Q201 - Q225)
        [
            ("What is Computer Security?", "Computer Security ka kya arth hai?", "Protection of computer systems and data from theft or damage", ["Protection of computer systems and data from theft or damage", "Increasing RAM speed", "Cleaning keyboard dust", "Designing web pages"]),
            ("What is Malware?", "Malware shabd kiska sankshipt roop hai?", "Malicious Software", ["Malicious Software", "Machine Software", "Manual Hardware", "Mega Application"]),
            ("Which of the following is an example of Malware?", "Inmein se kaun sa malware ka udaharan hai?", "Virus / Trojan / Worm", ["Virus / Trojan / Worm", "MS Word", "Antivirus", "Windows OS"]),
            ("What is a Computer Virus?", "Computer virus kya hota hai?", "A malicious program that replicates by copying itself into other programs", ["A malicious program that replicates by copying itself into other programs", "A hardware repairing tool", "A legal software update", "A network cable"]),
            ("What is a Trojan Horse in computer security?", "Trojan Horse kya hota hai?", "Malware disguised as legitimate software", ["Malware disguised as legitimate software", "A hardware speed booster", "An open-source browser", "A secure backup file"]),
            ("What is Ransomware?", "Ransomware kya hota hai?", "Malware that encrypts files and demands ransom for decryption", ["Malware that encrypts files and demands ransom for decryption", "A free utility software", "An internet speed booster", "A legitimate office tool"]),
            ("What is Spyware?", "Spyware ka kya karya hota hai?", "Software that secretly gathers information about a person or organization", ["Software that software secretly gathers information about a person or organization", "To speed up computer", "To print documents", "To clean cache"]),
            ("What is Adware?", "Adware kya hota hai?", "Software that automatically displays unwanted advertisements", ["Software that automatically displays unwanted advertisements", "Antivirus software", "System driver", "Spreadsheet tool"]),
            ("What is a Firewall used for in a computer system?", "Computer mein Firewall ka mukhya upyog kya hai?", "To monitor and filter incoming and outgoing network traffic", ["To monitor and filter incoming and outgoing network traffic", "To increase processing speed", "To cool down CPU", "To store backup files"]),
            ("What is Antivirus Software?", "Antivirus software ka kya upyog hai?", "To detect, prevent, and remove malware from a computer", ["To detect, prevent, and remove malware from a computer", "To create virus", "To browse internet", "To design graphics"]),
            ("What is Phishing?", "Phishing kya hoti hai?", "Fraudulent attempt to steal sensitive information by masquerading as trustworthy entity", ["Fraudulent attempt to steal sensitive information by masquerading as trustworthy entity", "Legal online shopping", "A computer game", "Hardware repair"]),
            ("What is Spam in computing?", "Computing mein Spam kya hota hai?", "Unwanted electronic junk messages sent in bulk", ["Unwanted electronic junk messages sent in bulk", "Important system updates", "Secure encrypted mail", "Backup files"]),
            ("What is Two-Factor Authentication (2FA)?", "Two-Factor Authentication (2FA) kya hai?", "A security process where user provides two different authentication factors", ["A security process where user provides two different authentication factors", "Using two passwords same time", "Having two computers", "Using two internet connections"]),
            ("What is Encryption?", "Encryption ka kya arth hai?", "Converting readable data into coded unreadable format for security", ["Converting readable data into coded unreadable format for security", "Deleting files permanently", "Compressing file size", "Scanning for virus"]),
            ("What is Decryption?", "Decryption ka kya arth hai?", "Converting encrypted coded data back into readable format", ["Converting encrypted coded data back into readable format", "Encrypting passwords", "Uninstalling software", "Formatting hard drive"]),
            ("What is a Hacker?", "Hacker kise kehte hain?", "A person who uses computer skills to gain unauthorized access to systems", ["A person who uses computer skills to gain unauthorized access to systems", "A software engineer who builds games", "A hardware technician", "An IT teacher"]),
            ("What is Ethical Hacking?", "Ethical Hacking kya hoti hai?", "Authorized hacking to find and fix security vulnerabilities", ["Authorized hacking to find and fix security vulnerabilities", "Stealing bank money", "Creating computer viruses", "Damaging servers"]),
            ("What is a Strong Password?", "Strong Password mein kya hona chahiye?", "Combination of uppercase, lowercase, numbers, and special characters", ["Combination of uppercase, lowercase, numbers, and special characters", "Only user name", "Simple 123456 number", "Phone number"]),
            ("What is Cyber Crime?", "Cyber Crime kya hota hai?", "Criminal activities carried out via computers or the internet", ["Criminal activities carried out via computers or the internet", "Playing offline video games", "Typing in MS Word", "Browsing YouTube"]),
            ("What is a Security Patch?", "Security Patch kya hota hai?", "A piece of software designed to update and fix security vulnerabilities", ["A piece of software designed to update and fix security vulnerabilities", "A computer virus", "A password protector", "A hardware cable"]),
            ("What is Data Backup?", "Data Backup ka kya arth hai?", "Creating a duplicate copy of important data for safety", ["Creating a duplicate copy of important data for safety", "Deleting old files", "Formatting hard disk", "Scanning for malware"]),
            ("What is Ad-blocker?", "Ad-blocker ka kya upyog hai?", "Software to block advertisements on web pages", ["Software to block advertisements on web pages", "To download files", "To send emails", "To play games"]),
            ("What is Identity Theft?", "Identity Theft kya hoti hai?", "Stealing someone's personal information to commit fraud", ["Stealing someone's personal information to commit fraud", "Changing computer wallpaper", "Forgetting password", "Deleting browser history"]),
            ("What is a Zero-Day Vulnerability?", "Zero-Day Vulnerability kya hoti hai?", "An unknown software security flaw that hackers exploit before fix is released", ["An unknown software security flaw that hackers exploit before fix is released", "A virus that deletes after zero days", "A safe password", "An expired antivirus"]),
            ("What is Biometric Security?", "Biometric Security mein kya upyog hota hai?", "Using unique physical characteristics like fingerprints or facial recognition", ["Using unique physical characteristics like fingerprints or facial recognition", "Using a 4-digit PIN", "Using a secret question", "Using a USB key"])
        ],
        # Part 10: Shortcut Keys, IT Terms & Miscellaneous (Q226 - Q250)
        [
            ("What is the shortcut key to Copy text?", "Text copy karne ki shortcut key kya hai?", "Ctrl + C", ["Ctrl + C", "Ctrl + V", "Ctrl + X", "Ctrl + P"]),
            ("What is the shortcut key to Paste text?", "Text paste karne ki shortcut key kya hai?", "Ctrl + V", ["Ctrl + V", "Ctrl + C", "Ctrl + X", "Ctrl + Z"]),
            ("What is the shortcut key to Cut text?", "Text cut karne ki shortcut key kya hai?", "Ctrl + X", ["Ctrl + X", "Ctrl + C", "Ctrl + V", "Ctrl + A"]),
            ("What is the shortcut key to Select All items?", "Sabhi items select karne ki shortcut key kya hai?", "Ctrl + A", ["Ctrl + A", "Ctrl + S", "Ctrl + F", "Ctrl + P"]),
            ("What is the shortcut key to Save a file?", "File save karne ki shortcut key kya hai?", "Ctrl + S", ["Ctrl + S", "Ctrl + O", "Ctrl + N", "Ctrl + P"]),
            ("What is the shortcut key to Print a file?", "File print karne ki shortcut key kya hai?", "Ctrl + P", ["Ctrl + P", "Ctrl + T", "Ctrl + R", "Ctrl + S"]),
            ("What is the shortcut key to Undo an action?", "Undo karne ki shortcut key kya hai?", "Ctrl + Z", ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + A"]),
            ("What is the shortcut key to Redo an action?", "Redo karne ki shortcut key kya hai?", "Ctrl + Y", ["Ctrl + Y", "Ctrl + Z", "Ctrl + R", "Ctrl + D"]),
            ("What is the shortcut key to Find words in a document?", "Words find karne ki shortcut key kya hai?", "Ctrl + F", ["Ctrl + F", "Ctrl + H", "Ctrl + G", "Ctrl + P"]),
            ("What is the shortcut key to open Replace dialog?", "Replace dialog kholne ki shortcut key kya hai?", "Ctrl + H", ["Ctrl + H", "Ctrl + F", "Ctrl + R", "Ctrl + E"]),
            ("What is the shortcut key to open New Tab in a web browser?", "Browser mein naya tab kholne ki shortcut key kya hai?", "Ctrl + T", ["Ctrl + T", "Ctrl + N", "Ctrl + W", "Ctrl + R"]),
            ("What is the shortcut key to close current browser tab?", "Current tab band karne ki shortcut key kya hai?", "Ctrl + W", ["Ctrl + W", "Ctrl + T", "Ctrl + N", "Ctrl + Q"]),
            ("What is the shortcut key to open Download history in a browser?", "Browser mein downloads history dekhne ki shortcut key kya hai?", "Ctrl + J", ["Ctrl + J", "Ctrl + H", "Ctrl + D", "Ctrl + B"]),
            ("What is the shortcut key to open History in a browser?", "Browser history kholne ki shortcut key kya hai?", "Ctrl + H", ["Ctrl + H", "Ctrl + J", "Ctrl + D", "Ctrl + T"]),
            ("What is the shortcut key to open Task Manager in Windows?", "Windows mein Task Manager kholne ki shortcut key kya hai?", "Ctrl + Shift + Esc", ["Ctrl + Shift + Esc", "Ctrl + Alt + Del", "Alt + F4", "Win + D"]),
            ("What is the shortcut key to lock Windows PC?", "Computer screen ko lock karne ki shortcut key kya hai?", "Windows Key + L", ["Windows Key + L", "Ctrl + L", "Alt + L", "Shift + L"]),
            ("What is the shortcut key to minimize all open windows and show desktop?", "Sabhi windows minimize karke desktop dekhne ki shortcut key kya hai?", "Windows Key + D", ["Windows Key + D", "Ctrl + D", "Alt + D", "F5"]),
            ("What is the shortcut key to open File Explorer?", "File Explorer kholne ki shortcut key kya hai?", "Windows Key + E", ["Windows Key + E", "Ctrl + E", "Alt + E", "F1"]),
            ("What does BIOS stand for?", "BIOS ka poora roop kya hota hai?", "Basic Input Output System", ["Basic Input Output System", "Binary Input Operating System", "Built-in Internal Operation Source", "Basic Internet Online Service"]),
            ("What does PDF stand for?", "PDF ka poora roop kya hota hai?", "Portable Document Format", ["Portable Document Format", "Printed Digital File", "Public Data Form", "Personal Doc Format"]),
            ("What does USB stand for?", "USB ka poora roop kya hota hai?", "Universal Serial Bus", ["Universal Serial Bus", "Universal System Board", "Unified Service Bus", "User Serial Bridge"]),
            ("What does LED stand for in monitors?", "Monitors mein LED ka poora roop kya hota hai?", "Light Emitting Diode", ["Light Emitting Diode", "Liquid Energy Display", "Low Emission Device", "Light Electric Display"]),
            ("What does LCD stand for in monitors?", "LCD ka poora roop kya hota hai?", "Liquid Crystal Display", ["Liquid Crystal Display", "Light Circuit Device", "Liquid Core Display", "Lasting Color Device"]),
            ("What is Artificial Intelligence (AI)?", "Artificial Intelligence (AI) kya hoti hai?", "Simulation of human intelligence in machines programmed to think", ["Simulation of human intelligence in machines programmed to think", "A computer repair tool", "A virus scanner", "An internet cable"]),
            ("What is the full form of IT in computer science?", "Computer science mein IT ka poora roop kya hota hai?", "Information Technology", ["Information Technology", "Internet Transmission", "Internal Tool", "Input Terminal"])
        ]
    ]

    # Combine all 10 parts into a flat list of 250 questions
    q_counter = 1
    for part_idx, part in enumerate(parts_data, start=1):
        for item in part:
            q_text = f"Q{q_counter}. {item[0]} ({item[1]})"
            questions.append({
                "question": q_text,
                "options": item[3],
                "answer_text": item[2]
            })
            q_counter += 1
            
    return questions

# Module 1 mein 250 unique questions set karna
data["modules"][0]["questions"] = generate_module_1_250()

# Baaki modules ke liye placeholders (Inhe bhi hum aage similar tareeqe se 250 banayenge)
for mod_idx in range(1, 4):
    temp_qs = []
    for i in range(1, 251):
        temp_qs.append({
            "question": f"Q{i}. Module {mod_idx+1} practice question number {i}?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer_text": "Option A"
        })
    data["modules"][mod_idx]["questions"] = temp_qs

# JSON file mein save karna
with open("tec_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Success! Module 1 ke poore 250 unique questions (10 parts mein batte hue) tec_questions.json mein generate ho gaye hain!")