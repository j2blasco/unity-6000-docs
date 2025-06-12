* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies-introduction.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Light sources](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-sources.html)
  * [Cookies](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html)
  * Introduction to cookies


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html)
Cookies
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies-apply.html)
Apply a cookie
# Introduction to cookies
![An example of baked fake caustics achieved using baked light cookies.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/updated-cookie.png) An example of baked fake caustics achieved using baked light cookies.
A cookie is a mask that you place on a light to create a shadow with a specific shape or color, which changes the appearance and intensity of the light.
Cookies are an efficient way of simulating complex lighting effects with minimal runtime performance impact. Effects you can simulate with cookies include caustics, soft shadows, and light shapes.
For example, the following illustration shows how you can simulate a real-time point light shadow with a light cookie. If there are no dynamic objects that can enter the area with a light cookie shadow, a user is unlikely to notice a difference between the cookie and a real-time shadow.
![Point light with a light cookie emulating shadows \(left\), and a point light without shadows \(right\)](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shadows/shadows-with-light-cookie.png)  
Point light with a light cookie emulating shadows (left), and a point light without shadows (right)
Spot lights with cookies can create the effect of light coming in from a window.
If you create a Texture that contains an alpha channel and assign it to the **Cookie** variable of the light, the cookie is projected from the light. The cookie’s alpha mask modulates the light’s brightness, creating light and dark spots on surfaces. This is a great way to add complexity or atmosphere to a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
## Render pipeline compatibility
See [render pipeline feature comparison](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html) for more information about support for cookies across **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
## Additional resources
  * [Unity forum: New Feature - Baked Light Cookies](https://forum.unity.com/threads/2020-1-new-feature-baked-light-cookies.848269/)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html)
Cookies
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies-apply.html)
Apply a cookie
