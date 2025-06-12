* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.IncrementUpdateCount.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).IncrementUpdateCount
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
public void IncrementUpdateCount(); 
### Description
Increment the update counter.
Call this method when you update a Texture from the GPU side, or you want to explicitly increment the counter.
```
using UnityEngine;  
  
public class RenderSomething
{
    RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) m_RT;  
  
    void Awake()
    {
        m_RT = new RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)(512, 512, 0);
    }  
  
    public void Render(Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) source)
    {
        Graphics.Blit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html)(source, m_RT);
        // We updated the render target on the GPU, so increment the update counter
        m_RT.IncrementUpdateCount();
    }
}

```

* * *
