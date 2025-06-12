* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-timeSinceStartup.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).timeSinceStartup
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
timeSinceStartup; 
### Description
The time since the editor was started. (Read Only)
This property contains the time since the editor was started, in seconds. Unlike [Time.realtimeSinceStartup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartup.html), this is not reset when starting play mode.  
  
Additional resources: [Time.realtimeSinceStartup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartup.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SimpleAutoSave.png)  
_Simple Editor Window that saves each 300 seconds the current Scene._
```
// Simple editor window that autosaves the working Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
// Make sure to have this window opened to be able to execute the auto save.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.SceneManagement;
using UnityEditor.SceneManagement;  
  
public class SimpleAutoSave : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static float saveTime = 300.0f;
    static double nextSave = 0;  
  
    static int autoSaveLabel = 1;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Simple autoSave")]
    static void Init()
    {
        SimpleAutoSave window = (SimpleAutoSave)GetWindowWithRect(
            typeof(SimpleAutoSave),
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 160, 60));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 80, 20), "Save Each:");
        EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(80, 10, 80, 20), saveTime + " secs");  
  
        double timeToSave = nextSave - EditorApplication.timeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-timeSinceStartup.html);  
  

        EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 30, 80, 20), "Next Save:");
        EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(80, 30, 80, 20), timeToSave.ToString("N1") + " secs");  
  
        this.Repaint();  
  
        // when time has reach zero then save the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
        if (EditorApplication.timeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-timeSinceStartup.html) > nextSave)
        {
            Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene = SceneManager.GetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetActiveScene.html)();
            string name = scene.name + autoSaveLabel;  
  
            EditorSceneManager.SaveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SaveScene.html)(scene, "Assets/wibble/" + name + ".unity", true);
            autoSaveLabel = autoSaveLabel + 1;
            nextSave = EditorApplication.timeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-timeSinceStartup.html) + saveTime;  
  
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Saved Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html): " + name);
        }
    }
}

```

* * *
