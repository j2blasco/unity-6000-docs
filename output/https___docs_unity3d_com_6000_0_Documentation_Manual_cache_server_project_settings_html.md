* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/cache-server-project-settings.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Caching assets](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html)
  * Cache Server Project Settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-mirror-instances.html)
Mirror multiple Unity Accelerator instances
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-metrics-reference.html)
Unity Accelerator Prometheus metrics reference
# Cache Server Project Settings reference
You can adjust how Unity Accelerator works with the Cache Server Project Settings. To open the Cache Server settings go to **Edit > Project Settings > Editor > Cache Server**
![Project Settings window, with the Cache Server settings displayed.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/accelerator-project-settings.png) Project Settings window, with the Cache Server settings displayed. **Setting** | **Description**  
---|---  
**Mode** | Choose whether to use the cache server. Choose from the following options: 
  * **Use global settings:** Uses the settings in the **Preferences** window (**Settings > Asset Pipeline > Unity Accelerator**).
  * **Enabled** : Enable the cache server.
  * **Disabled:** Disable the cache server.

  
**IP Address** | Input the **accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator)’s IP address and port.  
**Check Connection** | Select **Check Connection** to test the connectivity of the accelerator.  
**Namespace prefix** | Set a custom namespace for the server.  
**Download** | Enable downloads from the cache server.  
**Upload** | Enable uploads from the cache server.  
**TLS/SSL** | Enable encryption on the cache server.  
**Authentication (Using Unity ID)** | Enable authentication for the cache server using Unity ID.  
**Content Validation** | Select the level of content validation: Disabled, Upload Only, Enabled, Required.  
**Download Batch Size** | Set the size of download.  
## Additional resources
  * [Configure Unity Accelerator in the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-mirror-instances.html)
Mirror multiple Unity Accelerator instances
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-metrics-reference.html)
Unity Accelerator Prometheus metrics reference
