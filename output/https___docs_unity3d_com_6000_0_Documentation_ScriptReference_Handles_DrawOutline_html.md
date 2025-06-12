* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawOutline.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawOutline
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
public static void DrawOutline(GameObject[] objects, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) parentNodeColor, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) childNodeColor, float fillOpacity); 
## Declaration
public static void DrawOutline(GameObject[] objects, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, float fillOpacity); 
## Declaration
public static void DrawOutline(List<GameObject> objects, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) parentNodeColor, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) childNodeColor, float fillOpacity); 
## Declaration
public static void DrawOutline(List<GameObject> objects, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, float fillOpacity); 
## Declaration
public static void DrawOutline(int[] parentRenderers, int[] childRenderers, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) parentNodeColor, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) childNodeColor, float fillOpacity); 
## Declaration
public static void DrawOutline(int[] renderers, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, float fillOpacity); 
## Declaration
public static void DrawOutline(Renderer[] renderers, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) parentNodeColor, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) childNodeColor, float fillOpacity); 
## Declaration
public static void DrawOutline(Renderer[] renderers, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, float fillOpacity); 
### Parameters
Parameter | Description  
---|---  
objects | The GameObjects to outline.  
parentNodeColor | The color of the outline of the GameObjects provided explicitly in the `objects` parameter and the `parentRenderers` parameters. The alpha value controls the intensity of the outline.  
childNodeColor | The color of the outline of the GameObjects which are children to the GameObjects in the `objects` parameter. The alpha value controls the intensity of the outline.  
color | The color of the outline for the `objects` and `renderers`.  
parentRenderers | The instance IDs of the first set of Renderers. If you provide GameObjects or Renderers as parameters, these Renderers belong to the GameObjects provided explicitly in the parameters.  
childRenderers | The instance IDs of the second set of Renderers. If you provide GameObjects or Renderers as parameters, these Renderers belong to the child GameObjects of the objects provided in the parameters.  
fillOpacity | The opacity of the Renderers within each outline.  
renderers | The Renderers to outline.  
### Description
Draws an outline around the specified GameObjects in the Scene View.
This only applies to GameObjects that have Renderer components. You can only use this during a [EventType.Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html) event.  
  
Instead of passing in GameObjects or Renderers, you can also use Renderer [instance IDs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html). This improves performance because Unity doesn't need to get the instance IDs from the GameObjects or Renderers every time you call this function.  
  
NOTE: Overloads that take GameObject[], Renderer[] or List<GameObject> as arguments are there for convenience, using them might result in additional allocations that cause additional garbage collection. To avoid performance or memory issues, use these overloads only when drawing a relatively small number of outlines (consider providing renderer instance IDs directly if the number of outlines exceeds 100).  
  
The alpha values of `parentNodeColor` and `childNodeColor` control the intensity of the outline, 0 makes it completely transparent and 1 makes it fully opaque.  
  
The `fillOpacity` controls the weight of the color multiplier for the Renderer. Higher `fillOpacity` values make the color more intense and leave the original object less visible.  
  
Additional resources: [Handles.DrawCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawCamera.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
namespace UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html)
{
    [CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)))]
    public class CustomInspector : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
    {
        private GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] objects;  
  
        public void OnEnable()
        {
            // Note: If you use FindGameObjectsWithTag in a Prefab Stage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.html) that you opened from a Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html),
            // it includes GameObjects from that Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html). Instead use:
            // var renderers = StageUtility.GetCurrentStage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageUtility.GetCurrentStage.html)().FindComponentsOfType<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
            // to explicitly specify where to get the GameObjects from.
            objects = GameObject.FindGameObjectsWithTag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindGameObjectsWithTag.html)("Player");  // populate the objects array with game objects
        }  
  
        public void OnSceneGUI()
        {
            // draw the outline with an alpha of 0.5
            if (Event.current.type == EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html))
                Handles.DrawOutline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawOutline.html)(objects, Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html), Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), 0.1f);
        }
    }
}

```

* * *
