* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ManagingYourUnityLicense.html

  * [Install and upgrade](https://docs.unity3d.com/6000.0/Documentation/Manual/install-and-upgrade.html)
  * [Licenses and activation](https://docs.unity3d.com/6000.0/Documentation/Manual/LicensesAndActivation.html)
  * Manage your license through the command line


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LicenseActivationMethods.html)
License activation methods
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ManualActivationGuide.html)
Manual license activation
# Manage your license through the command line
To use Unity, you need an activated license.
The primary [license activation method](https://docs.unity3d.com/6000.0/Documentation/Manual/LicenseActivationMethods.html) for Unity Pro and Unity Personal is the [Unity Hub](https://docs.unity3d.com/hub/manual/ManageLicense.html). For information about activating a Unity Industry license, refer to the Unity Support article, [How to activate or return a Unity Industry license](https://support.unity.com/hc/en-us/articles/9113620465428-How-do-I-activate-or-return-my-Unity-Industry-license-).
The following information covers an alternate method to Unity Hub for [activating](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagingYourUnityLicense.html#license-activation-cli) and [returning](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagingYourUnityLicense.html#license-return-cli) a license for Unity Pro, by using the command line. You might consider this method in situations such as:
  * You have internet access, but you use Unity in headless mode (without a GUI) for automated tasks, such as builds and tests.
  * You have internet access, but you’re unable or unwilling to install the Unity Hub.


**Note** : The following procedures don’t apply to Unity Personal. To activate a license for Unity Personal, log in to the Unity Hub. To return a Personal license, log out of the Unity Hub.
If you don’t know your Unity license information, speak to the [Owner](https://docs.unity.com/cloud/en-us/organizations/members-groups-roles) of your license. Owners can assign a seat to you via the [Organization](https://docs.unity.com/cloud/en-us/organizations), or you can contact Unity Customer Service.
## Activate a license from the command line
Before activating your Unity license by using the command line, make sure that the license file folder exists. Refer to [Unity license file location](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html#licensefilefolders) in [License troubleshooting](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html). Also make sure that you have write permission to this folder.
### macOS
Enter the following command into the Terminal to launch Unity and activate your license:
```
<unity-command-location> -quit -batchmode -serial SB-XXXX-XXXX-XXXX-XXXX-XXXX -username 'name@example.com' -password 'XXXXXXXXXXXXX'

```

**Notes:**
  * Replace `<unity-command-location>` with the [full path to your Unity Editor application](https://docs.unity3d.com/hub/manual/AddEditor.html#locate-the-editor-program-file), concatenated with `/Contents/MacOS/Unity`. For example, if you installed a `2022.2.0b4` Editor to the default location, `<unity-command-location>` is:
```
/Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app/Contents/MacOS/Unity

```

  * If you want to activate a named user license without activating its serial key, use the same command, but omit your serial key after specifying the `-serial` keyword:
```
... -serial -username 'name@example.com' -password 'XXXXXXXXXXXXX'

```



#### macOS example 1
The following example activates a named user license without activating its serial key:
```
/Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app/Contents/MacOS/Unity -quit -batchmode -serial -username 'name@example.com' -password 'XXXXXXXXXXXXX'

```

  

#### macOS example 2
The following example activates a serial key. If your plan supports named user licensing, it activates that license and also activates its serial key.
```
/Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app/Contents/MacOS/Unity -quit -batchmode -serial SB-XXXX-XXXX-XXXX-XXXX-XXXX -username 'name@example.com' -password 'XXXXXXXXXXXXX'

```

  

### Windows
Enter the following command into the Command Prompt to launch Unity and activate your license:
```
"<editor-installation-location>" -quit -batchmode -serial E3-XXXX-XXXX-XXXX-XXXX-XXXX -username name@example.com -password XXXXXXXXXXXXX

```

**Notes:**
  * Replace `<editor-installation-location>` with the [full path to your Unity Editor application](https://docs.unity3d.com/hub/manual/AddEditor.html#locate-the-editor-program-file). For example, if you installed a `2022.2.0b4` Editor to the default location, `<editor-installation-location>` is:
```
C:\Program Files\Unity\Hub\Editor\2022.2.0b4\Editor\Unity.exe

```

  * If you want to activate a named user license without activating its serial key, use the same command, but omit your serial key after specifying the `-serial` keyword:
```
... -serial -username 'name@example.com' -password 'XXXXXXXXXXXXX'

```



#### Windows example 1
The following example activates a named user license without activating its serial key:
```
"C:\Program Files\Unity\Hub\Editor\2022.2.0b4\Editor\Unity.exe" -quit -batchmode -serial -username name@example.com -password XXXXXXXXXXXXX

```

  

#### Windows example 2
The following example activates a serial key. If your plan supports named user licensing, it activates that license and also activates its serial key.
```
"C:\Program Files\Unity\Hub\Editor\2022.2.0b4\Editor\Unity.exe" -quit -batchmode -serial E3-XXXX-XXXX-XXXX-XXXX-XXXX -username name@example.com -password XXXXXXXXXXXXX

```

  

### Next steps and troubleshooting
Wait several seconds after running this command to give Unity enough time to communicate with the license server. If activation fails, you can open the [Editor.log](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html) for information. For any activation errors, check [Activation issues](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html) to find a solution for your issue.
## Returning the license through the command line
### macOS
Enter the following command into the Terminal to return the license:
```
<unity-command-location> -quit -batchmode -returnlicense -username 'name@example.com' -password 'XXXXXXXXXXXXX'

```

Replace `<unity-command-location>` with the [full path to your Unity Editor application](https://docs.unity3d.com/hub/manual/AddEditor.html#locate-the-editor-program-file), concatenated with `/Contents/MacOS/Unity`. For example, if you installed a `2022.2.0b4` Editor to the default location, `<unity-command-location>` is:
```
/Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app/Contents/MacOS/Unity

```

  

#### macOS example
```
/Applications/Unity/Hub/Editor/2022.2.0b4/Unity.app/Contents/MacOS/Unity -quit -batchmode -returnlicense -username 'name@example.com' -password 'XXXXXXXXXXXXX'

```

  

### Windows
Enter the following into the Command Prompt to return the license 
```
"<editor-installation-location>" -quit -batchmode -returnlicense -username name@example.com -password XXXXXXXXXXXXX

```

Replace `<editor-installation-location>` with the [full path to your Unity Editor application](https://docs.unity3d.com/hub/manual/AddEditor.html#locate-the-editor-program-file). For example, if you installed a `2022.2.0b4` Editor to the default location, `<editor-installation-location>` is:
```
C:\Program Files\Unity\Hub\Editor\2022.2.0b4\Editor\Unity.exe

```

  

#### Windows example
```
"C:\Program Files\Unity\Hub\Editor\2022.2.0b4\Editor\Unity.exe" -quit -batchmode -returnlicense -username name@example.com -password XXXXXXXXXXXXX

```

  

### Next steps and troubleshooting
Wait a few seconds after running this command to give Unity enough time to communicate with the license server. You can use the Hub to confirm that you returned your license by opening the Preferences menu (![Cog](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/hubPref.png)) and selecting **Licenses**. If you experience issues, refer [Troubleshooting](https://docs.unity3d.com/6000.0/Documentation/Manual/ActivationFAQ.html).
## Additional resources
  * [License activation methods](https://docs.unity3d.com/6000.0/Documentation/Manual/LicenseActivationMethods.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LicenseActivationMethods.html)
License activation methods
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ManualActivationGuide.html)
Manual license activation
