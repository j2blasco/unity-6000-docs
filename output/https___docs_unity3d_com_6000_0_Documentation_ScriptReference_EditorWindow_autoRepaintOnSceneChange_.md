* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-autoRepaintOnSceneChange.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).autoRepaintOnSceneChange
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
autoRepaintOnSceneChange; 
### Description
Enable this property to automatically repaint the window when the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) is modified.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/CameraViewer.png)   
_Editor Window that renders what the main camera is "seeing"._
```
// Simple script that lets you render the main camera in an Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window.

using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class CameraViewer : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera;
    RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) renderTexture;
    Image[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html) image;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) Viewer")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) editorWindow = GetWindow(typeof(CameraViewer));
        editorWindow.autoRepaintOnSceneChange = true;
        editorWindow.Show();
    }

    public void Awake()
    {
        renderTexture = new RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)((int)position.width,
            (int)position.height,
            (int)RenderTextureFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html));
    }

    public void OnEnable()
    {
        camera = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);
    }

    void CreateGUI()
    {
        image = new Image[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html)();
        image.image = renderTexture;
        image.style.width = Length.Percent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.Percent.html)(100);
        image.style.height = Length.Percent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.Percent.html)(100);
        rootVisualElement.Add(image);
    }

    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (renderTexture.width != position.width ||
            renderTexture.height != position.height)
            renderTexture = new RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)((int)position.width,
                (int)position.height,
                (int)RenderTextureFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html));
            image.image = renderTexture;    

        if (camera != null)
        {
            camera.targetTexture = renderTexture;
            camera.Render();
            camera.targetTexture = null;
        }    
    }
}

```

* * *
