* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.html

# Device
class in UnityEngine.iOS
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Interface into iOS specific functionality.
### Static Properties
Property | Description  
---|---  
[advertisingIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-advertisingIdentifier.html) | Advertising ID.  
[advertisingTrackingEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-advertisingTrackingEnabled.html) | Is advertising tracking enabled.  
[deferSystemGesturesMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-deferSystemGesturesMode.html) | Defer system gestures until the second swipe on specific edges.  
[generation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-generation.html) | The generation of the device. (Read Only)  
[hideHomeButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-hideHomeButton.html) | Specifies whether the home button should be hidden in the iOS build of this application.  
[iosAppOnMac](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-iosAppOnMac.html) | Indicates whether the process is an iOS app running on a Mac.  
[lowPowerModeEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-lowPowerModeEnabled.html) | Indicates whether Low Power Mode is enabled on the device.  
[runsOnSimulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-runsOnSimulator.html) | Returns true if the process is an iOS app running on a Simulator.  
[systemVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-systemVersion.html) | iOS version.  
[vendorIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-vendorIdentifier.html) | Vendor ID.  
[wantsSoftwareDimming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-wantsSoftwareDimming.html) | Indicates whether the screen may be dimmed lower than the hardware is normally capable of by emulating it in software.  
### Static Methods
Method | Description  
---|---  
[RequestStoreReview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.RequestStoreReview.html) | Request App Store rating and review from the user.  
[ResetNoBackupFlag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.ResetNoBackupFlag.html) | Set file flag to be included in iCloud/iTunes backup.  
[SetNoBackupFlag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.SetNoBackupFlag.html) | Set file flag to be excluded from iCloud/iTunes backup. This uses NSURLIsExcludedFromBackupKey. Note that you should set this property each time you save a file.  
* * *
