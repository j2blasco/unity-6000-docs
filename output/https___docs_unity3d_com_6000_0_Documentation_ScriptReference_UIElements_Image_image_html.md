* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image-image.html

#  [Image](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html).image
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
[Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image; 
### Description
The texture to display in this image. If you assign a `Texture` or `Texture2D`, the Image element will resize and show the assigned texture. 
The following example creates an `Image` element and assigns a texture to it. 
```
using UnityEngine;
using UnityEngine.UIElements;  
  
public class AddImageExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) myTexture;    
    void OnEnable()
    {
        var root = GetComponent<UIDocument[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument.html)>().rootVisualElement;       
        var imageElement = new Image[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html)();
        imageElement.image = myTexture;        
        root.Add(imageElement);
    }
}

```

* * *
