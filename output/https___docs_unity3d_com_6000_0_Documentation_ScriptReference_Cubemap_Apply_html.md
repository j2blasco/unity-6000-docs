* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.Apply.html

#  [Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html).Apply
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
## Declaration
public void Apply(bool updateMipmaps = true, bool makeNoLongerReadable = false); 
### Parameters
Parameter | Description  
---|---  
updateMipmaps | When the value is `true`, Unity recalculates mipmap levels, using mipmap level 0 as the source. The default value is `true`.  
makeNoLongerReadable | When the value is `true`, Unity deletes the texture in CPU memory after it uploads it to the GPU, and sets [isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) to `false`. The default value is `false`.  
### Description
Copies changes you've made in a CPU texture to the GPU.
For most types of textures, Unity can store a copy of the texture in both CPU and GPU memory.  
  
The CPU copy is optional. If the CPU copy exists, you can read from and write to the CPU copy more flexibly than the GPU copy. But to render the updated texture, you must use `Apply` to copy it from the CPU to the GPU.  
  
If you set `makeNoLongerReadable` to `true`, Unity deletes the CPU copy of the texture after it uploads it to the GPU.  
  
You usually only set `updateMipmaps` to `false` if you've already updated the mipmap levels, for example using [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.SetPixels.html).  
  
`Apply` is an expensive operation because it copies all the pixels in the texture even if you've only changed some of the pixels, so change as many pixels as possible before you call it. 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) cubeMap;  
  
    void Start()
    {
        cubeMap.SetPixel(CubemapFace.PositiveX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.PositiveX.html), 0, 0, Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
        // Do more changes to the faces...
        cubeMap.Apply(); // Apply the stuff done to the Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html).
    }
}

```

* * *
