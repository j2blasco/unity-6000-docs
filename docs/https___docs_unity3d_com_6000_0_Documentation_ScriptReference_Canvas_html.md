* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html

# Canvas
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
/
Implemented in:[UnityEngine.UIModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIModule.html)
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
Element that can be used for screen rendering.
Elements on a canvas are rendered AFTER Scene rendering, either from an attached camera or using overlay mode.
```
using System.Collections;
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UI;  
  
// Create a Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html) that holds a Text GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) myGO;
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) myText;
        Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html) myCanvas;
        Text text;
        RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html) rectTransform;  
  
        // Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html)
        myGO = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)();
        myGO.name = "TestCanvas";
        myGO.AddComponent<Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html)>();  
  
        myCanvas = myGO.GetComponent<Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html)>();
        myCanvas.renderMode = RenderMode.ScreenSpaceOverlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderMode.ScreenSpaceOverlay.html);
        myGO.AddComponent<CanvasScaler>();
        myGO.AddComponent<GraphicRaycaster>();  
  
        // Text
        myText = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)();
        myText.transform.parent = myGO.transform;
        myText.name = "wibble";  
  
        text = myText.AddComponent<Text>();
        text.font = (Font[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.html))Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)("MyFont");
        text.text = "wobble";
        text.fontSize = 100;  
  
        // Text position
        rectTransform = text.GetComponent<RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html)>();
        rectTransform.localPosition = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0);
        rectTransform.sizeDelta = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(400, 200);
    }
}

```

### Properties
Property | Description  
---|---  
[additionalShaderChannels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-additionalShaderChannels.html) | Get or set the mask of additional shader channels to be used when creating the Canvas mesh.  
[cachedSortingLayerValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-cachedSortingLayerValue.html) | Cached calculated value based upon SortingLayerID.  
[isRootCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-isRootCanvas.html) | Is this the root Canvas?  
[normalizedSortingGridSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-normalizedSortingGridSize.html) | The normalized grid size that the canvas will split the renderable area into.  
[overridePixelPerfect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-overridePixelPerfect.html) | Allows for nested canvases to override pixelPerfect settings inherited from parent canvases.  
[overrideSorting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-overrideSorting.html) | Allows for nested canvases to override the Canvas.sortingOrder from parent canvases.  
[pixelPerfect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-pixelPerfect.html) | Forces pixel alignment for elements in the canvas. It only applies when Canvas.renderMode is set to Screen Space.  
[pixelRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-pixelRect.html) | Get the render rect for the Canvas.  
[planeDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-planeDistance.html) | How far away from the camera is the Canvas generated? It only applies when Canvas.renderMode is set to RenderMode.ScreenSpaceCamera.  
[referencePixelsPerUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-referencePixelsPerUnit.html) | The number of pixels per unit that is considered the default.  
[renderingDisplaySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-renderingDisplaySize.html) | Returns the canvas display size based on the selected render mode and target display.  
[renderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-renderMode.html) | Is the Canvas in World or Overlay mode?  
[renderOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-renderOrder.html) | The render order in which the canvas is being emitted to the Scene. (Read Only)  
[rootCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-rootCanvas.html) | Returns the Canvas closest to root, by checking through each parent and returning the last canvas found. If no other canvas is found then the canvas will return itself.  
[scaleFactor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-scaleFactor.html) | Scales the entire canvas, ensuring it fits the screen. It only applies when Canvas.renderMode is set to Screen Space.  
[sortingLayerID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-sortingLayerID.html) | Unique ID of the Canvas' sorting layer.  
[sortingLayerName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-sortingLayerName.html) | Name of the Canvas' sorting layer.  
[sortingOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-sortingOrder.html) | Canvas' order within a sorting layer.  
[targetDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-targetDisplay.html) | For Overlay mode, display index on which the UI canvas will appear.  
[updateRectTransformForStandalone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-updateRectTransformForStandalone.html) | Should the Canvas size be updated based on the render target when a manual Camera.Render call is performed.  
[vertexColorAlwaysGammaSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-vertexColorAlwaysGammaSpace.html) | Should the Canvas vertex color always be in gamma space before passing to the UI shaders in linear color space work flow.  
[worldCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-worldCamera.html) |  Camera used for sizing the Canvas when in Screen Space - Camera. Also used as the Camera that events will be sent through for a World Space Canvas.  
### Static Methods
Method | Description  
---|---  
[ForceUpdateCanvases](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.ForceUpdateCanvases.html) | Force all canvases to update their content.  
[GetDefaultCanvasMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.GetDefaultCanvasMaterial.html) | Returns the default material that can be used for rendering normal elements on the Canvas.  
[GetETC1SupportedCanvasMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.GetETC1SupportedCanvasMaterial.html) | Gets or generates the ETC1 Material.  
### Events
Event | Description  
---|---  
[preWillRenderCanvases](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-preWillRenderCanvases.html) | Event that is called just before Canvas rendering happens.  
[willRenderCanvases](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-willRenderCanvases.html) | Event that is called just before Canvas rendering happens.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
