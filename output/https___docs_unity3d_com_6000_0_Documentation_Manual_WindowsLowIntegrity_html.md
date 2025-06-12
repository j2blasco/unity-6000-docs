* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsLowIntegrity.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Windows](https://docs.unity3d.com/6000.0/Documentation/Manual/Windows.html)
  * [Develop for Windows](https://docs.unity3d.com/6000.0/Documentation/Manual/windows-develop.html)
  * Windows integrity control


[](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsDebugging-forensic.html)
Set up forensic debugging for Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
Windows Player: IL2CPP Scripting Backend
# Windows integrity control
The **Mandatory Integrity Control** security feature on Windows devices allocates an integrity level (IL) to all applications and processes. The device’s operating system or database constrains a user’s or initiator’s ability to access or perform other operations on an _object/target_ (such as files, memory, or directories). Both the initiator and the object are allocated an IL, with low as the most restricted access. When the initiator attempts to access the object, their ILs are compared. The initiator can’t access the object if it has a lower IL than the object.
For more information about integrity levels, see Microsoft’s [Mandatory Integrity Control](https://docs.microsoft.com/en-us/windows/win32/secauthz/mandatory-integrity-control) documentation. 
Windows Standalone player can detect if it’s running at low integrity level. For more information, see Microsoft’s documentation on [Designing Applications to Run at a Low Integrity Level](https://msdn.microsoft.com/en-us/library/bb625960.aspx). In this case, one of the following things might happen:
  * The log file is written to `%USERPROFILE%\AppData\LocalLow\CompanyName\ProductName`
  * PlayerPrefs is saved to `HKCU\Software\AppDataLow\Software\CompanyName\ProductName`


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsDebugging-forensic.html)
Set up forensic debugging for Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
Windows Player: IL2CPP Scripting Backend
