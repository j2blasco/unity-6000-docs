* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.html

# GridBrushBase
class in UnityEngine
/
Inherits from:[ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
/
Implemented in:[UnityEngine.TilemapModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.TilemapModule.html)
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
Base class for authoring data on a grid with grid painting tools like paint, erase, pick, select and fill.
Inheriting this class and/or creating brush asset instances from your inherited class, you can create custom brushes which react to high level grid events like paint, erase, pick, select and fill.
```
using UnityEngine;  
  
// Paints two Prefabs in checkerboard pattern
[CreateAssetMenu]
public class CheckerboardBrush : GridBrushBase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabA;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabB;  
  
    public override void Paint(GridLayout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.html) grid, GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) brushTarget, Vector3Int[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.html) position)
    {
        bool evenCell = Mathf.Abs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Abs.html)(position.y + position.x) % 2 > 0;
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) toBeInstantiated = evenCell ? prefabA : prefabB;  
  
        if (toBeInstantiated != null)
        {
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) newInstance = Instantiate(toBeInstantiated, grid.CellToWorld(position), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
            newInstance.transform.SetParent(brushTarget.transform);
        }
    }
}

```

### Public Methods
Method | Description  
---|---  
[BoxErase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.BoxErase.html) | Erases data on a grid within the given bounds.  
[BoxFill](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.BoxFill.html) | Box fills tiles and GameObjects into given bounds within the selected layers.  
[ChangeZPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.ChangeZPosition.html) | Changes the Z position of the GridBrushBase.  
[Erase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.Erase.html) | Erases data on a grid within the given bounds.  
[Flip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.Flip.html) | Flips the grid brush in the given FlipAxis.  
[FloodFill](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.FloodFill.html) | Flood fills data onto a grid given the starting coordinates of the cell.  
[Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.Move.html) | Move is called when user moves the area previously selected with the selection marquee.  
[MoveEnd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.MoveEnd.html) | MoveEnd is called when user has ended the move of the area previously selected with the selection marquee.  
[MoveStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.MoveStart.html) | MoveEnd is called when user starts moving the area previously selected with the selection marquee.  
[Paint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.Paint.html) | Paints data into a grid within the given bounds.  
[Pick](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.Pick.html) | Picks data from a grid given the coordinates of the cells.  
[ResetZPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.ResetZPosition.html) | Resets Z position changes of the GridBrushBase.  
[Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.Rotate.html) | Rotates all tiles on the grid brush with the given RotationDirection.  
[Select](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridBrushBase.Select.html) | Select an area of a grid.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
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
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
* * *
