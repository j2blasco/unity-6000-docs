* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-intro.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
  * [Web templates](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-templates.html)
  * Using Web templates


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-templates.html)
Web templates
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-add.html)
Add a custom Web template
# Using Web templates
When you build a Web project, Unity embeds the Player in a HTML page such that a browser can open it. A Web template is a configuration setting that lets you control the appearance of this HTML page, so that you can test, demonstrate, and preview your Web application in a browser.
To access Web templates:
  1. Go to [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) (menu: **Edit** > **Project Settings** > **Player**).
  2. Set the platform-specific settings to Web.
  3. Open **Resolution and Presentation**.

![Image of Player Resolution and Presentation window. ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/WebGLResolutionandPresentationWindow.png) Image of Player Resolution and Presentation window. 
## Built-in templates
By default, the **Web Template** setting has the following options:
  * **Default** : A white page with a loading bar on a grey canvas.
  * **Minimal** : A minimal Web template with that includes the necessary boilerplate code to run the Web content.
  * **PWA:** A **Progressive Web App** A software application that’s delivered through the web. It uses certain browser features to create a user experience on par with a native application. [More info](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProgressiveWebApp) including a web manifest file and service worker code.


These built-in HTML pages are useful for testing and demonstrating a minimal Player.
## Custom templates
You can also use JavaScript to build and supply your own Web templates to host the Player. This is useful for production purposes, so that you can preview the Player hosted in the page where it’s deployed. For example, if the Unity Player content interacts with other elements in the page via the external call interface, test it with a page that contains those interacting elements.
## Additional resources
  * [Add a custom Web template](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-add.html)
  * [Web template structure and instantiation](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-structure.html)
  * [Web template variables](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-variables.html)
  * [Web template build configuration and interaction](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-build-configuration.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-templates.html)
Web templates
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-add.html)
Add a custom Web template
