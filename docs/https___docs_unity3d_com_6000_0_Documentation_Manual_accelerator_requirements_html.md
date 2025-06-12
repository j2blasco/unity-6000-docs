* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-requirements.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Caching assets](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html)
  * Unity Accelerator requirements


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)
Introduction to Unity Accelerator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-installer.html)
Install Unity Accelerator with the installer
# Unity Accelerator requirements
You can install Unity **Accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator) in the following ways:
  * [Through the Accelerator Installer](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-installer.html)
  * [Through Docker Hub](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-docker.html)


After you install Unity Accelerator, you must [configure it in the Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html).
## Prerequisites
Install Unity Accelerator on each network your team works on. You must have a machine running on your local network that can host a cache server with the following requirements:
## Operating system
The local host must run one of the following operating systems:
  * Linux (Ubuntu 18.04 or later). You must install Unity Accelerator as a root user.
  * Windows Server 2008R2 or Windows 7 or higher (64 bit)
  * macOS 10.12 or higher (64 bit)


## Storage size
The local host must have enough local storage space to host most of your project’s files. Ideally, the storage space is on a solid-state drive separate from the drive that hosts your operating system. 
  * **Recommended storage size** : The equivalent of one local Library folder for each active development branch on every platform you’re developing for. For example, if you’re building for iOS, Android, and **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL), and your team is working on 5 branches at the same time (mainline, staging, and 3 feature branches), and your average Library folder is 5 GB, then you need 75 GB storage.
  * **Minimum storage size** : The equivalent of one local Library folder for every platform you’re developing for. For example, if you’re building for iOS, Android, and WebGL, and your average Library folder is 5 GB, then you need 15 GB storage.


## Memory size
The local host needs as much memory as is reasonably affordable. The minimum is 2 GB of RAM, but if more memory is available the operating system uses it to buffer cached items, resulting in higher performance for commonly accessed items.
  * The recommended RAM size is enough RAM to store one entire copy of the Library folder. Unity Accelerator uses a LRU (Least Recently Used) cache to self-manage the RAM. Ideally you want enough RAM to store as many entire copies of the Library folder as are being actively worked on (target platforms * active branches). This prevents the disk storage from being accessed as much.
  * At a minimum, you must have RAM the size of the largest asset in your Library folder across all target platforms. If you don’t know, have at least 2 GB of RAM.


## Network requirements
The local host must be attached to the same network as your team, or locally routable with appropriate firewall policies that allow access to cache server’s IP address and port (TCP). Unity Accelerator’s performance is dependent on network bandwidth, and the bandwidth of end-users’ connectivity path to the cache server instance.
There are no built-in access controls in the Unity Accelerator, so it’s best practice to host it behind a VPN or another restrictive firewall so that non-authorised users can’t access sensitive data. 
## Additional resources
  * [Install Unity Accelerator with the installer](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-installer.html)
  * [Install Unity Accelerator with Docker Hub](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-docker.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)
Introduction to Unity Accelerator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-installer.html)
Install Unity Accelerator with the installer
