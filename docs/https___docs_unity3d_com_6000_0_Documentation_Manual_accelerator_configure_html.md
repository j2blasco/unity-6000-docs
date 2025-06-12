* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Caching assets](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html)
  * Configure Unity Accelerator in the Editor


[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-verify-version.html)
Verify the Unity Accelerator version
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-stop-restart.html)
Stop and restart Unity Accelerator
# Configure Unity Accelerator in the Editor
To configure your Unity Editor to use Unity **Accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator), perform the following steps:
  1. Open the **Project Settings** window (**Edit** > **Project Settings**) and select **Editor** from the left panel.
  2. Under the **Cache Server** section, set **Mode** to **Enabled**.
  3. Fill in the **IP address** with the cache server’s IP address and port (default `10080`). To get the IP address, the setup wizard displays this information at the end of setup in this format: `[IP]:[Port].`You can also find this information in the `unity-accelerator.log` file.
  4. Select the **Check Connection** button to test connectivity.

![Project Settings window, with the Cache Server settings displayed.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/accelerator-project-settings.png) Project Settings window, with the Cache Server settings displayed.
If the Check Connection test fails, check the IP and port values are correct and that the IP is accessible from your current machine.
## Customize settings
You can configure further settings such as a different namespace prefix, and upload and download preferences in the **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) window. Note that the namespace prefix is used as the prefix to 3 different namespaces, one for metadata, one for import artifacts and one for **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) compilation artifacts.
It’s best practice to set a different namespace prefix from the default, so that you can ensure isolation from other projects and can help prevent cache corruption. You could use a namespace prefix that includes your project name, and the Unity version you’re using, for example `GameProjectX_6000.1`. To set the namespace, edit the **Namespace prefix** field.
You can also individually disable uploading or downloading. For example, for larger teams it is often good practice to only allow developers to pull from the cache, and only allow a single user or a build machine to upload. When used in combination with source control, the single user or build machine would check out the latest source, and perform a full import of any new asset data and upload the resulting artifacts to the Accelerator. Developers would then be able to pull from source control and pull the import artifacts from the Accelerator saving them the time importing them. This might help mitigate any issues with corrupted assets, ensuring that everyone recieves the same import data from a single source of truth.
You can also configure Unity Accelerator to use the global settings (**Unity** > **Settings** > **Asset Pipeline**) which is used by default for all projects unless overridden in the Project Settings. 
For more information on the settings refer to [Cache Server Project Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/cache-server-project-settings.html).
## Connectivity status
The status of the Unity Accelerator’s connectivity is displayed in the bottom right corner of the Unity Editor window.
![Unity Accelerator connectivity](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AcceleratorConnect.png) Unity Accelerator connectivity
## Additional resources
  * [Install Unity Accelerator with the installer](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-installer.html)
  * [Install Unity Accelerator with Docker Hub](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-docker.html)
  * [Cache Server Project Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/cache-server-project-settings.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-verify-version.html)
Verify the Unity Accelerator version
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-stop-restart.html)
Stop and restart Unity Accelerator
