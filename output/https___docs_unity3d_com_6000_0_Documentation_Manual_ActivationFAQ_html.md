* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html

  * [Install and upgrade](https://docs.unity3d.com/6000.0/Documentation/Manual/install-and-upgrade.html)
  * [Licenses and activation](https://docs.unity3d.com/6000.0/Documentation/Manual/LicensesAndActivation.html)
  * License troubleshooting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ManualActivationCmdMac.html)
Submit a license request from a command line and browser (macOS, Linux)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuides.html)
Upgrade Unity
# License troubleshooting
This section provides information on the following licensing management issues:
  * [Activation issues](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html#activation)
  * [Issues with returns](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html#returns)
  * [Unity license file location](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html#licensefilefolders)
  * [Answers to other questions](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html#other)
  * [Additional resources](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html#more-help)


## Activation issues
The following issues can cause error codes or other problems during the activation process:
**Issue** | **Solution**  
---|---  
**No internet access** |  **Serial-based license:**  
You can activate your serial-based license with a license request. For more information, refer to [Manual license activation](https://docs.unity3d.com/6000.0/Documentation/Manual/ManualActivationGuide.html).   
  
**Named user license:**  
You can’t activate a [named user license](https://docs.unity3d.com/6000.0/Documentation/Manual/LicenseOverview.html) without internet access.  
**Security settings block Unity** | Review your firewall, proxy, or internet security settings. They might be blocking Unity from sending and receiving data about your license file. For more information, refer to [Use Unity through web proxies](https://docs.unity3d.com/6000.0/Documentation/Manual/ent-proxy-autoconfig.html).  
**No write privileges for saving the license file** | Grant or request write permissions to the user account you are using to activate a license. This often occurs in closed networks, such as those at workplaces and schools. Contact your IT administrator to find out whether there are any restrictions in place. For a list of directories where you need write privileges, refer to [Unity license file location](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html#licensefilefolders).  
**License fails to recognize your computer** | Major operating system changes or updates might affect your computer’s ID, which might cause your license to stop recognizing your computer. Refer to [Can I use my licence with different operating systems](https://support.unity.com/hc/en-us/articles/360021433091-Can-I-use-my-licence-with-different-operating-systems) and these categories of Unity Support articles:  
  
- [Activations and Management](https://support.unity.com/hc/en-us/sections/202242003-Activations-and-Management)  
- [Licensing and Payments](https://support.unity.com/hc/en-us/sections/201104799-Licensing-and-Payments)  
**Unity’s license servers are down** | Refer to the [Unity Cloud System Status Page](https://status.cloud.unity3d.com/) for status updates on all Unity servers.  
**Too many license activations** | Return your license if you no longer need it for a specific computer. Choose from the following methods to return a license:  
  
- **Unity Hub** : Return serial-based licenses by using the **Preferences** window > **Licenses** tab > **Return license** button. Return named user licenses by signing out of the Unity Hub.  
- **Command line** : Return serial-based licenses following the instructions in [Manage your license through the command line](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagingYourUnityLicense.html).  
- **ID Portal** : Return serial-based licenses and named user licenses from the [Unity ID Portal](https://id.unity.com/) > **My Accounts** > **My Seats**. You can use this method even if you don’t have access to the computer whose license you’re returning, or if that computer’s bindings changed.  
  
You must return your license before you switch computers. You must also return your license before you make any hardware changes or operating system changes to your computer. If you fail to return the license, the Unity license server sees a request from another computer and informs you that you have reached your activation limit for the license.  
  
If you get this message but you think it’s an error, you can return all licenses at once, and then reactivate each computer, as needed.  
**Account credentials not recognized** | Make sure you enter your details correctly. Passwords are case sensitive, so make sure you enter them as registered. To reset your password, go to the Unity ID Portal: <https://id.unity.com/en/password/new>.  
  
You can also receive failed login or activation errors if you or your build server exceeds the login rate limit, which is 10 login attempts per minute for a specific user.  
  
If you still have problems logging in, submit a request in the [Unity Support portal](https://support.unity.com/hc/en-us).  
## Issues with returning licenses
The following issues can cause error codes or other problems while returning your license:
**Issue** | **Solution**  
---|---  
**You can’t return your license because you can’t access the computer where your license was activated** | 1. Go to <https://id.unity.com/> and log in with your Unity ID.  
2. Select **My Account** > **My Seats** in the side menu.  
3. Select the activation you want to deactivate, then select **Remove selected activations**. If you want to return all activations in one action, select **Disable all activations**.  
  
If you have licenses activated on other computers, you need to re-activate them later.  
  
If you still can’t return your license, and your license is for a paid plan, submit a request in the [Unity Support portal](https://support.unity.com/hc/en-us). For serial-based licenses, include these details:  
- The serial key you were using on the computer.  
- The (local network) name of the computer you can’t access.  
- The order or invoice number used to purchase your subscription.  
  
For named user licenses, include these details:  
- Organization name.  
- User name.  
- Subscription name, if you have multiple subscriptions within your organization.  
  
The Support Team can return your license manually if you provide the previous information; however, it can take some time.  
## Unity license file location
**Question** | **Answer**  
---|---  
**Where is my serial-based license file stored?** | - Windows: `%PROGRAMDATA%\Unity\Unity_lic.ulf`  
  
- macOS: `/Library/Application\ Support/Unity/Unity_lic.ulf`  
  
- Linux: `~/.local/share/unity3d/Unity/Unity_lic.ulf`  
  
**Note** : If Windows User Account Control (UAC) has restricted your access to `C:\ProgramData\Unity`, you can find your `ulf` file at:  
`C:\Users\(username)\AppData\Local\VirtualStore\ProgramData\Unity`  
(UAC can restrict access if the folder is deleted or if you start the Unity Editor with administrative permissions first time.)  
**Where is my named user license file stored?** | - Windows: `%LOCALAPPDATA%\Unity\licenses\UnityEntitlementLicense.xml`  
  
- macOS: `~/Library/Unity/licenses/UnityEntitlementLicense.xml`  
  
- Linux: `~/.config/unity3d/Unity/licenses/UnityEntitlementLicense.xml`  
**Where is my floating license file stored?** | - Windows: `%LOCALAPPDATA%\Unity\licenses\<token-id>.xml`  
  
- macOS: `~/Library/Unity/licenses/<token-id>.xml`  
  
- Linux: `~/.config/unity3d/Unity/licenses/<token-id>.xml`  
## Answers to other questions
**Question** | **Answer**  
---|---  
**How do I know what type of license I have?** | Refer to [Licensing overview](https://docs.unity3d.com/6000.0/Documentation/Manual/LicenseOverview.html).  
**How many computers can I install my copy of Unity on?** | Every paid commercial Unity license allows one person to use Unity on two computers that they have exclusive use of. It doesn’t matter where the computers are physically located or what operating system they’re running.   
  
Educational licenses sold via Unity or any one of Unity’s resellers are good only for a single activation. The same limit applies to Trial licenses (Unity 4.x only), unless otherwise stated.  
  
The free version of Unity can’t be licensed by a commercial, educational, non-profit, or government entity whose gross revenues or budget exceeds the financial threshold identified in the [Unity Editor Software Terms](https://unity.com/legal/editor-terms-of-service/software) section of the [Unity Terms of Service](https://unity.com/legal).  
  
If you are a Legal Entity, you can’t combine files developed with the free version of Unity with any files developed by you (or by any third party) through the use of Unity Pro.  
  
For more information about license usage, refer to [Legal Information](https://unity.com/legal).  
**Can I use the latest version of Unity with a serial key from a previous version?** | If you have a serial key for Unity Editor 2017 or later, open the Unity Hub and activate the serial key. Refer to [Activate with a serial number](https://docs.unity3d.com/hub/manual/ManageLicense.html#activate-with-a-serial-number).  
  
If you have a serial key for Unity version 5.x, use that version of the Editor. For activation information, refer to [Version 5.6 documentation](https://docs.unity3d.com/560/Documentation/Manual/LicensesAndActivation.html).  
  
To get a new Unity license, go to the [online store](https://store.unity.com/).  
  
If you’re unsure about your license options, [contact Unity using this form](https://create.unity.com/contact-unity-expert).  
**I have two serial-based licenses, each with an add-on I require. How do I activate them in unison on my computer?** | You can use a single license on only one computer at a time. You can’t activate two or more serial-based licenses at the same time on one computer.  
**I have seats for multiple subscriptions assigned to my Unity ID. How do I activate them in unison on my computer?** | Named user licenses for all your assigned seats are automatically activated when you sign in to the Unity Hub.  
**How can I use different Unity versions?** | You can install multiple versions of the Unity Editor on a single computer. However, you can activate only one serial-based license on a computer at a time. This means that you can’t concurrently run an older version of Unity (2017 or earlier) and another version released after 2017, if you use serial-based licenses for both. These versions require different licenses. You can, however, use an older version of Unity with a serial-based license and a newer version of Unity (2019.4 or later), if the latter uses named user licensing or floating licensing.   
  
If you need to use different Unity versions with distinct serial-based licenses, you need to manage the activation process. This process involves activating the required license for the version you intend to use and deactivating the licenses for the other versions.   
  
Another way to manage this process is to activate the required licenses and store their license files in a backup folder on your computer. Then, before launching a specific version of Unity, delete the existing license file (with a `.ulf` extension) from the Unity [license folder](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html#licensefilefolders), and copy the appropriate license file from your backup folder into the Unity license folder. This process ensures that the correct license is active for the version you intend to use.  
  
For further help, submit a request in the [Unity Support portal](https://support.unity.com/hc/en-us).  
**What should I do if I’m planning to replace a hardware component or change my operating system?** | You must [return your license](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagingYourUnityLicense.html) before you change any hardware or change the operating system on your computer. You must also [return your license](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagingYourUnityLicense.html) before you switch computers. If you fail to return the license, the Unity license server sees a request from another computer and informs you that you have reached your activation limit for the license.  
**What do I do if I can’t log in because my company prevents me from accepting the Terms of Service?** | Contact your sales representative.  
**How do I track and remove activated licenses across all of the computers where I’ve activated my licenses?** | To track and remove named user licenses, go to [Unity ID](https://id.unity.com) and select **My Account** > **My Seats**.  
**Which versions of the Unity Editor work with named user licenses?** | Any Editor in the 2021 stream or later. For the 2020 Editor, you must use 2020.2.2 or later. For the 2019 Editor, you must use 2019.4.27 or later.  
**Why don’t I see the Return license button in Unity Hub?** | The **Return license** button doesn’t display if you have a named user license for Unity Personal. The only way to return a named user license for Unity Personal is by signing out of the Unity Hub.  
**I unintentionally disagreed with Terms of Service while getting a named user license for Unity Personal. How can I activate this license?** | Sign out of Unity Hub and sign in again. The Unity Hub will display the confirmation window again, where you can agree with Terms of Service to activate the license.  
**How do I activate a license for an older editor?** | If you want to use your paid subscription on a older Unity Editor (2019.3 or earlier), you must activate the license with the serial key. For more information refer to [Activate a license from the command line](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagingYourUnityLicense.html#license-activation-cli).  
## Additional resources
  * [Licenses](https://support.unity.com/hc/categories/201268913-Licenses) (Unity Support category)
  * [Activations and Management](https://support.unity3d.com/hc/en-us/sections/202242003-Activations-and-Management) (Unity Support category)
  * [Unity Customer Services](https://support.unity3d.com/hc/en-us/requests/new?ticket_form_id=65905) (Unity Support request)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ManualActivationCmdMac.html)
Submit a license request from a command line and browser (macOS, Linux)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuides.html)
Upgrade Unity
