* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-updateCount.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).updateCount
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
updateCount; 
### Description
This counter is incremented when the Texture is updated.
Note: If you perform an update from the GPU side, you should increment the counter yourself. (For instance, when blitting into a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)). (see [IncrementUpdateCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.IncrementUpdateCount.html)).
```
using UnityEngine;
using System.Collections.Generic;  
  
public class MyTextureCache
{
    struct TextureCacheMeta
    {
        internal int index;
        internal uint updateCount;
    }  
  
    Dictionary<Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html), TextureCacheMeta> m_TextureMetas = new Dictionary<Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html), TextureCacheMeta>();
    RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) m_Cache;  
  
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) cache { get { return m_Cache; } }  
  
    public int CacheTexture(Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html))
    {
        var index = -1;
        TextureCacheMeta meta;
        if (m_TextureMetas.TryGetValue(Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html), out meta))
        {
            if (meta.updateCount != Texture.updateCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-updateCount.html))
            {
                // Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) has changed since last caching
                // So blit again into the cache Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)
                BlitTextureAt(meta.index, Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html));
                meta.updateCount = Texture.updateCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-updateCount.html);
                m_TextureMetas[Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)] = meta;
            }
        }
        else
        {
            index = GetNextIndex();
            if (index < 0)
            {
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Invalid index");
                return -1;
            }  
  
            m_TextureMetas[Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)] = new TextureCacheMeta
            {
                index = index,
                updateCount = Texture.updateCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-updateCount.html)
            };
        }
        return index;
    }  
  
    void BlitTextureAt(int index, Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)) { /* copy pixels in cache */ }
    int GetNextIndex() { return -1; /* Get next index to use in the cache */ }
}

```

* * *
