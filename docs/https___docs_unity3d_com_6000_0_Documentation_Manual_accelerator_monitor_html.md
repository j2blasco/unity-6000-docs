* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-monitor.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Caching assets](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html)
  * Monitor Unity Accelerator


[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-stop-restart.html)
Stop and restart Unity Accelerator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-command-line.html)
Use Unity Accelerator on the command line
# Monitor Unity Accelerator
Unity **Accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator) has a built-in dashboard to monitor and configure changes.
The URL to access your dashboard is `http://ip:port/dashboard` where `ip:port` is the IP and port number of the Unity Accelerator you have installed. Note that the default http port is `80` but you can change this during installation. If left as default `80`, then it doesn’t need to be specified here.
![Accelerator configuration dashboard](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AcceleratorConfig.png) Accelerator configuration dashboard
Each Unity Accelerator hosts [Prometheus metric reports](https://prometheus.io/) as `http://ip:port/metrics`, which you can query from the local network. For a full list of metrics monitoring, refer to [Unity Accelerator Prometheus metrics reference](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-metrics-reference.html). The full configuration of Unity Accelerator is available through its unity-accelerator.cfg file.
## Additional resources
  * [Unity Accelerator Prometheus metrics reference](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-metrics-reference.html)
  * [Configure Unity Accelerator in the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-stop-restart.html)
Stop and restart Unity Accelerator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-command-line.html)
Use Unity Accelerator on the command line
