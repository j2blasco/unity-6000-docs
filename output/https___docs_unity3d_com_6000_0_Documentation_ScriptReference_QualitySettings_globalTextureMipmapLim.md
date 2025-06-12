* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).globalTextureMipmapLimit
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
globalTextureMipmapLimit; 
### Description
Indicates how many of the highest-resolution mips of each texture Unity does not upload at the given quality level. To set more specific mipmap limits, you can flag textures to ignore mipmap limits or assign them to mipmap limit groups.
Set this value to 1 to use the second mip of each texture, so all textures are half size. Set this value to 2 to use the third mip of each texture, so all textures are quarter size. This trend remains consistent as values increase. The default value is zero.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/mipmap-stripping.png)  
_Mip levels of five textures. The first (unused) texture is set to 0 and increases by 1 mip level until the fifth texture which is set to 4. The size of each texture is a quarter of the texture preceding it._  
  
You can use this limit to decrease video memory requirements for running your content on low-end devices.  
  
At run time, if you set globalTextureMipmapLimit to a mipmap value that has been stripped, Unity sets the value to the closest mipmap value that has not been stripped. For additional information regarding mipmap stripping, see [PlayerSettings.mipStripping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-mipStripping.html).  
  
The Global Texture Mipmap Limit only works on 2D textures and 2D texture arrays. It cannot adjust other texture types such as cubemaps. This setting has no effect on non-mipmapped textures. Also, note that the Virtual Texturing system does not consider mipmap limits either. For textures with mixed usage (see [Texture2D.vtOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-vtOnly.html)), mipmap limits, streaming and stripping are only active for those instances that aren't rendered using Virtual Texturing. Similar to how the GPU load for regular textures can be managed by setting mipmap limits (or using Texture Streaming), the GPU load for the VT system can be managed by updating the GPU cache sizes (see [GPUCacheSetting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.GPUCacheSetting.html)).  
  
The global texture mipmap limit does not affect the following types of 2D textures: * Built-in editor resources such as UI icons and elements * Textures created at run time which are not readable, for example, after calling Apply with makeNoLongerReadable set to true * Non persistent textures, when [EditorUtility.IsPersistent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html) returns false * Rendertargets * Terrain masks  
  
Queries for the width and height of the texture object return the original, non-limited sizes. You may have to take this into account if you perform special sampling or processing with textures subject to the global limit and you use globalTextureMipmapLimit > 1.  
  
When the globalTextureMipmapLimit changes, Unity synchronously re-uploads all loaded textures affected by the global texture mipmap limit.  
  
At the same time, Unity requests an asynchronous re-upload for textures that are using the Texture Streaming system and affected by the global texture mipmap limit.  
  
Be aware: the system may take a few frames to apply a new **globalTextureMipmapLimit** value to textures that already had an upload request running before the change.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Use half-size textures.
        QualitySettings.globalTextureMipmapLimit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html) = 1;
    }
}

```

Additional resources: [TextureMipmapLimitGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html).
* * *
