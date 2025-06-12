* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceUniqueIdentifier.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).deviceUniqueIdentifier
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
deviceUniqueIdentifier; 
### Description
A unique device identifier. It's guaranteed to be unique for every device (Read Only).
**iOS** : Uses [UIDevice.identifierForVendor ](https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor) to generate a unique device identifier.  
  
**macOS** : Uses [kIOPlatformUUIDKey](https://developer.apple.com/documentation/iokit/kioplatformuuidkey) to generate a unique device identifier.  
  
**Android:** [SystemInfo.deviceUniqueIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceUniqueIdentifier.html) always returns the md5 of ANDROID_ID. (See <https://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID>). Note that since Android 8.0 (API level 26) ANDROID_ID depends on the app signing key. That means "unsigned" builds (which are by default signed with a debug keystore) will have a **different value** than signed builds (which are signed with a key provided in the player settings). Also when [allowing Google Play to sign your app](https://developer.android.com/studio/publish/app-signing#app-signing-google-play), this value will be different when testing locally built app which is signed with the upload key and app downloaded from the Google Play which will be signed with the "final" key.  
  
**Windows Store Apps** : uses AdvertisingManager::AdvertisingId for returning unique device identifier, if option in 'PC Settings -> Privacy -> Let apps use my advertising ID for experiences across apps (turning this off will reset your ID)' is disabled, Unity will fallback to HardwareIdentification::GetPackageSpecificToken().Id.  
  
**Windows Standalone** : returns a hash from the concatenation of strings taken from the following [Computer System Hardware Classes](https://msdn.microsoft.com/en-us/library/windows/desktop/aa389273\(v=vs.85\).aspx): 
  * Win32_BaseBoard::SerialNumber
  * Win32_BIOS::SerialNumber
  * Win32_OperatingSystem::SerialNumber


Will return [SystemInfo.unsupportedIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-unsupportedIdentifier.html) on platforms which don't support this property.
* * *
