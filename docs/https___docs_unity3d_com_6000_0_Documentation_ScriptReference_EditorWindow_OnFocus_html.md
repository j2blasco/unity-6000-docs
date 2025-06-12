* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnFocus.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).OnFocus()
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
### Description
Called when the window gets keyboard focus.
Additional resources: [OnLostFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnLostFocus.html).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/OrthographicPreviewer.png)  
_Preview your camera in orthographic mode when you select the window._
```
// Simple script that lets you preview your main camera in
// Orthographic view when selected.

using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class OrthographicPreview : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) renderTexture;
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera;
    Image[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html) image;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Orthographic Previewer")]
    static void Init()
    {
        OrthographicPreview window =
            (OrthographicPreview)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(OrthographicPreview), true, "My Empty Window");
        window.Show();
    }

    void OnEnable()
    {
        int w = (int)this.position.width;
        int h = (int)this.position.height;

        image = new Image[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html)();
        renderTexture = new RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)(w, h, 32, RenderTextureFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html));
        camera = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);
    }
    
    void OnDisable()
    {
        Object.DestroyImmediate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html)(renderTexture);
    }

    void CreateGUI()
    {
        var buttonClose = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        buttonClose.text = "Close";
        buttonClose.clicked += () =>
        {
            camera.orthographic = false;
            this.Close();
        };
        rootVisualElement.Add(buttonClose);

        if (renderTexture != null)
        {
            image.image = renderTexture;
            rootVisualElement.Add(image);          
        }
    }

    void OnFocus()
    {
        Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html) = camera.transform;
        camera.orthographic = true;
    }

    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        int w = (int)this.position.width;
        int h = (int)this.position.height;
        if (renderTexture.width != w || renderTexture.height != h)
        {
            Object.DestroyImmediate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html)(renderTexture);
            renderTexture = new RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)(w, h, 32, RenderTextureFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html));
            image.image = renderTexture;
        }

        if (camera != null)
        {
            camera.targetTexture = renderTexture;
            camera.Render();
            camera.targetTexture = null;
        }
    }

    void OnLostFocus()
    {
        camera.orthographic = false;
    }
}

```

* * *
