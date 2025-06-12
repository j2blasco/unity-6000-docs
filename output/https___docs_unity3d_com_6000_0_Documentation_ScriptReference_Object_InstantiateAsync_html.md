* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html

#  [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html).InstantiateAsync
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Object.html "Go to Object Component in the Manual")
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, [InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) parameters, CancellationToken cancellationToken); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) parameters, CancellationToken cancellationToken); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int count); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int count, [InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) parameters, CancellationToken cancellationToken); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int count, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int count, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int count, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) parameters, CancellationToken cancellationToken); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int count, ReadOnlySpan<Vector3> positions, ReadOnlySpan<Quaternion> rotations); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int count, ReadOnlySpan<Vector3> positions, ReadOnlySpan<Quaternion> rotations, [InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) parameters, CancellationToken cancellationToken); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int count, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
## Declaration
public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int count, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent, ReadOnlySpan<Vector3> positions, ReadOnlySpan<Quaternion> rotations); 
### Parameters
Parameter | Description  
---|---  
original | An existing object that you want to make a copy of.  
count | The number of new copies to create.  
parent | The parent that will be assigned to the new object or objects.  
position | The position for the new object or objects.  
rotation | The rotation for the new object or objects.  
positions | The read only span of positions for the new object or objects. The length of the array can be less than `count`, in which case Unity uses position[i % count].  
rotations | The read only span of rotations for the new object or objects. The length of the array can be less than `count`, in which case Unity uses rotation[i % count].  
parameters | A struct containing all the parameters  
### Returns
**AsyncInstantiateOperation <T>** An asynchronous operation that contains the resulting objects. 
### Description
Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.
The operation is mainly asynchronous, but the last stage involving integration and awake calls is executed on the main thread. The operation can be cancelled, or the integration stage can be delayed using allowSceneActivation. It is possible to yield a return operation or call its WaitForCompletion() method to finish the operation in a synchronized way.  
  
For extra control you can use the overrides that take an [InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) struct. This includes extra options like deciding between using local or world space, or to specify a target scene for the objects.
* * *
