* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-texture-compression.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * Texture compression in Web


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-video.html)
Video playback in Web
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-embeddedresources.html)
Embedded resources in Web
# Texture compression in Web
Use texture **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) in the Web platform to create builds that target platforms based on the **texture compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureCompression) formats they support.
## Texture compression formats
Desktop and mobile devices support different texture compression formats. If you want your Web application to use compressed textures on both types of browsers, you must first choose a supported texture compression format.
To run your game on both desktop and mobile browsers with compressed textures, you might want to create two builds targeting:
  * Desktop browsers with DXT set as the texture compression format.
  * Mobile browsers with adaptable scalable texture compression (ASTC) set as the texture compression format.


## Precedence for compression format settings
You can set the default texture compression format for your Web application from either the [Web build settings](https://docs.unity3d.com/6000.0/Documentation/Manual/web-build-settings.html) window or the Web [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) window. Before you set the texture compression format, it’s important to decide which of these settings take precedence. The texture compression format value you set in build settings has priority over the value you set in Player settings. By default, the Unity Editor sets the build settings value to **Use Player Settings**.
**Note:** The Editor serializes the texture compression in build settings in the `Library` folder. This means that it’s not managed by **version control** A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VersionControl).
You can also customize the texture compression format for individual textures. The value you set for an individual **texture overrides** Platform-specific settings that allow you to set the resolution, file size with associated memory size requirements, pixel dimensions, and quality of your Textures for each target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureOverrides) the default texture compression format value. For information on how to change the **texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat) of individual textures, refer to [Texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
## Set the default compression format
You can set the default texture compression format for your Web application using either build settings or Player settings. The texture compression format value you set in build settings has priority over the value you set in Player settings. By default, the Unity Editor sets the build settings value to **Use Player Settings**.
To select a default texture compression format using build settings:
  1. Select **File** > **Build Profiles**.
  2. From the list of platforms in the **Platform** panel, select **Web**.
  3. Select a compression format from the **Texture Compression** drop-down menu.


To select a default texture compression format using Player Settings:
  1. Select **File** > **Build Profiles**.
  2. From the list of platforms in the **Platform** panel, select **Web**.
  3. Select **Player Settings** > **Other Settings**.
  4. Select a compression format from the **Texture compression format** drop-down menu.


For an example on how to simultaneously create builds for both desktop browsers and mobile browsers with their corresponding texture compression formats, refer to [Create builds for desktop and mobile browsers from a script](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-texture-compression.html#desktop+mobile).
## Create builds for desktop and mobile browsers from a script
You can run a build for both desktop browsers and mobile browsers with the corresponding texture compression formats simultaneously using a script. For example:
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System.Diagnostics;
using System.IO;
using UnityEditor.Build.Reporting;

public class comboBuild
{
    //This creates a menu item to trigger the dual builds https://docs.unity3d.com/ScriptReference/MenuItem.html 

    [MenuItem("Game Build Menu/Dual Build")]
    public static void BuildGame()
    {
      //This builds the player twice: a build with desktop-specific texture settings (WebGL_Build)
      //as well as mobile-specific texture settings (WebGL_Mobile),
      //and combines the necessary files into one directory (WebGL_Build)
      
      string dualBuildPath    = "WebGLBuilds";
      string desktopBuildName = "WebGL_Build";
      string mobileBuildName  = "WebGL_Mobile";

      string desktopPath = Path.Combine(dualBuildPath, desktopBuildName);
      string mobilePath  = Path.Combine(dualBuildPath, mobileBuildName);
      string[] scenes = new string[] {"Assets/scene.unity"};

      EditorUserBuildSettings.webGLBuildSubtarget = WebGLTextureSubtarget.DXT;
      BuildPipeline.BuildPlayer(scenes, desktopPath, BuildTarget.WebGL, BuildOptions.Development); 

      EditorUserBuildSettings.webGLBuildSubtarget = WebGLTextureSubtarget.ASTC;
      BuildPipeline.BuildPlayer(scenes,  mobilePath, BuildTarget.WebGL, BuildOptions.Development); 

      // Copy the mobile.data file to the desktop build directory to consolidate them both
      FileUtil.CopyFileOrDirectory(Path.Combine(mobilePath, "Build", mobileBuildName + ".data"), Path.Combine(desktopPath, "Build", mobileBuildName + ".data"));
    }  
}

```

You can modify the [Web template’s](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-templates.html) `index.html` file to select the appropriate data file if there’s support for the texture compression format extension:
```
// choose the data file based on whether there's support for the ASTC texture compression format
      var dataFile = "/{{{ DATA_FILENAME }}}";                                  
      var c = document.createElement("canvas");                                 
      var gl = c.getContext("webgl");                                      
      var gl2 = c.getContext("webgl2");                                    
      if ((gl && gl.getExtension('WEBGL_compressed_texture_astc')) || (gl2 &&   
              gl2.getExtension('WEBGL_compressed_texture_astc'))) {             
        dataFile =  "/WebGL_Mobile.data";                                       
      }                                                                         

      var buildUrl = "Build";
      var loaderUrl = buildUrl + "/{{{ LOADER_FILENAME }}}";                    
      var config = {                                                            
        dataUrl: buildUrl + dataFile,                                           
        frameworkUrl: buildUrl + "/{{{ FRAMEWORK_FILENAME }}}",                 
#if USE_WASM                                                                    
        codeUrl: buildUrl + "/{{{ CODE_FILENAME }}}",                           
#endif                                                                          
#if MEMORY_FILENAME                                                             
        memoryUrl: buildUrl + "/{{{ MEMORY_FILENAME }}}",                       
#endif
#if SYMBOLS_FILENAME                                                            
        symbolsUrl: buildUrl + "/{{{ SYMBOLS_FILENAME }}}",                     
#endif                                                                          
        streamingAssetsUrl: "StreamingAssets",                                
        companyName: {{{ JSON.stringify(COMPANY_NAME) }}},
        productName: {{{ JSON.stringify(PRODUCT_NAME) }}},
      productVersion: {{{ JSON.stringify(PRODUCT_VERSION) }}},                
        showBanner: unityShowBanner,                                            
     };  


```

## Additional resources
  * [Build your Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building.html)
  * [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-video.html)
Video playback in Web
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-embeddedresources.html)
Embedded resources in Web
