* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.purchasing.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Packages](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages-all.html)
  * [Released packages](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-safe.html)
  * In App Purchasing 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/com.havok.physics.html)
Havok Physics for Unity 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.inputsystem.html)
Input System 
# In App Purchasing
[com.unity.purchasing](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAP.html) ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/iconRel.png)
## Description
IMPORTANT UPGRADE NOTES:  
  
If updating from Unity IAP (com.unity.purchasing + the Asset Store plugin) versions 2.x to version 3.x, complete the following actions in order to resolve compilation errors:  
1. Move IAPProductCatalog.json and BillingMode.json  
FROM: Assets/Plugins/UnityPurchasing/Resources/  
TO: Assets/Resources/.  
2. Move AppleTangle.cs and GooglePlayTangle.cs  
FROM: Assets/Plugins/UnityPurchasing/generated  
TO: Assets/Scripts/UnityPurchasing/generated.  
3. Remove all remaining Asset Store plugin folders and files in Assets/Plugins/UnityPurchasing from your project.  
  
PACKAGE DESCRIPTION:  
  
With Unity IAP, setting up in-app purchases for your game across multiple app stores has never been easier.  
  
This package provides:  
  
One common API to access all stores for free so you can fully understand and optimize your in-game economy  
Automatic coupling with Unity Analytics to enable monitoring and decision-making based on trends in your revenue and purchase data across multiple platforms  
Support for iOS, Mac, tvOS, Google Play, Windows, and Amazon app stores(*).  
Support to work with the Unity Distribution Portal to synchronize catalogs and transactions with other app stores  
Client-side receipt validation for Apple App Store and Google Play  
  
After installing this package, open the Services Window to enable In-App Purchasing to use these features. 
## Version information
### Released for Unity
Package version 4.12.2 is released for Unity Editor version 6000.0.
### Compatible with Unity
These package versions are available in Unity version 6000.0:
**Documentation location:** | **State** | **Versions available:**  
---|---|---  
[com.unity.purchasing@5.0](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAP.html) | compatible | 5.0.0-pre.1, 5.0.0-pre.2, 5.0.0-pre.3, 5.0.0-pre.4, 5.0.0-pre.5  
[com.unity.purchasing@4.12](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAP.html) | released | 4.12.2  
## Keywords
[purchasing](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-keys.html#purchasing) , [iap](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-keys.html#iap) , [unity](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-keys.html#unity)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/com.havok.physics.html)
Havok Physics for Unity 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.inputsystem.html)
Input System 
