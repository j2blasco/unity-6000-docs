* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-browsercompatibility.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-intro.html)
  * Web browser compatibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-intro.html)
Web introduction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-technical-overview.html)
Technical limitations
# Web browser compatibility
This page gives an overview of Unity’s Web platform support for desktop and mobile browsers.
## Web browser compatibility for desktop
Unity’s Web platform support for desktop browsers differs depending on the browser. It supports browsers providing the following conditions are true:
  * The browser is **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) 2 capable.
  * The browser is HTML 5 standards-compliant.
  * The browser is 64-bit and supports WebAssembly.


The Unity Web platform supports some compressed **texture formats** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat). For information on the compressed texture formats that Unity WebGL supports, refer to [Choose a GPU texture format by platform](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-choose-format-by-platform.html).
Web platform supports the following desktop browsers:
**Desktop Browser** | **Desktop Platforms**  
---|---  
Google Chrome | Windows, macOS, Linux  
Mozilla Firefox | Windows, macOS, Linux  
Apple Safari | macOS  
Microsoft Edge | Windows, macOS, Linux  
**Notes:**
  * The Web platform also supports the latest version of the Chromium-based Edge browser.
  * Apple Safari doesn’t support WebGL 2 in versions before Safari 15.
  * Apple Safari doesn’t support IndexedDB for content running in an iFrame.
  * On Linux, you might have to install Advanced Audio Coding (AAC) codec support via a package manager (for example, the GStreamer package).


## Web browser compatibility for mobile
The Unity Web platform supports some mobile browsers. To use a Web application on a mobile device, you have a few options:
  * Run the application in your mobile browser.
  * Use WebView to embed the application into native apps.
  * Use a **Progressive Web App** A software application that’s delivered through the web. It uses certain browser features to create a user experience on par with a native application. [More info](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProgressiveWebApp) (PWA) template.


Unity’s Web platform supports the following mobile browsers:
**Mobile Browser** | **Mobile Platform**  
---|---  
iOS Safari 15 and newer | iOS  
Chrome 58 and newer | Android  
**Note** : Use the latest browser versions for the best experience. Older versions might have issues that affect performance or prevent Unity content from running.
* * *
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-intro.html)
Web introduction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-technical-overview.html)
Technical limitations
