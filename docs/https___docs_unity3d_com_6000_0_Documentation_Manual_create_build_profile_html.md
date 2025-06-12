* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Build profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)
  * Create and manage build profiles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)
Introduction to build profiles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profile-scene-list.html)
Manage scenes in your build
# Create and manage build profiles
Create and manage **build profiles** A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) to configure your application for multiple platforms.
# Create a build profile
To create a build profile, use the following steps:
  1. Navigate to **File** > **Build Profiles**.
  2. In the **Build Profiles** window, select **Add Build Profile** to open the **Platform Browser** window. The **Platform Browser** window presents a list of supported platforms that include desktop, mobile, web, and **closed platforms** Includes platforms that require confidentiality and legal agreements with the platform provider for using their developer tools and hardware. These platforms aren’t open to development unless you have an established relationship with the provider. For example PlayStation®, Game Core for Xbox®, and Nintendo®.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Closedplatform).
  3. In the **Platform Browser** window, select the platform that you want to build your application on. If the selected platform isn’t currently installed on your machine, select **Install with Unity Hub** and follow the installation instructions. Before installing any platform module, refer to the [system requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html) page.
  4. Select **Add Build Profile**.
  5. Select the required [platform settings](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html).
  6. Select **Switch Profile** to set the new build profile as the active profile. This will attach an **Active** badge to the build profile name.


**Note** : If you plan to deploy your application on a closed platform, check the license requirements. For further information, refer to [Platform Module Installation](https://unity.com/platform-installation).
## Create a build profile from a platform profile
You can duplicate an existing platform profile and create a new build profile from it. To do that, right click your selected platform and select **Copy to new profile**. 
## Manage build profiles
To manage your build profiles, right-click on any build profile name. These options allow you to do the following:
  * Copy to a new build profile.
  * Rename a build profile.
  * Delete a build profile.


**Note** : There are no limits to how many build profiles you can have in a project.
## Additional resources
  * [Build Profiles window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html)
  * [Build Profiles scripting API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)
Introduction to build profiles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profile-scene-list.html)
Manage scenes in your build
