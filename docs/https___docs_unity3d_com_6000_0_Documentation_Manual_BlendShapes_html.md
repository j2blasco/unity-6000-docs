* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/BlendShapes.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animation clips](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)
  * [Animation window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)
  * Work with blend shapes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-AnimationWindowEvent.html)
Add an Animation Event
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AvatarCreationandSetup.html)
Humanoid Avatar
# Work with blend shapes
## Prepare the artwork
Once you have set up blend shapes in your 3D modeling application, do the following:
  1. In your 3D modeling application, enable these export settings: 
     * Enable exporting animation.
     * Enable exporting blend shapes for deformed models.
  2. Export your selection to an .fbx file.
  3. [Import your FBX file](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html) into Unity.
  4. Select the newly imported Model in the Hierarchy window. The **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window displays the **BlendShapes** section containing all the blend shapes under the [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html) component.
  5. For each listed blend shape, you can change its influence (weighting) to the default shape, where:
  6. `0` means the blend shape has no influence.
  7. `100` means the blend shape has full influence.


## Create animations In Unity
To create a blend animation:
  1. Open the Animation window (from the main Unity menu: **Window** > **Animation** > **Animation**).
  2. Select the **Animation Clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) where you want to add the blend shape animation. You can select **Create New Clip** to create a new Animation Clip.
  3. Click **Add Property** and select **[Your Character]** > **[Your Character Body]** > **Skinned Mesh Renderer** and select the blend shape you want to animate.
  4. Select the added blend shape property, adjusting the **keyframes** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) and blend weights, and set keyframes.


To preview your animation, click **Play** in the Editor window or the Animation window.
## Scripting access
You can also set the blend weights through scripting using functions like [GetBlendShapeWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.GetBlendShapeWeight.html) and [SetBlendShapeWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.SetBlendShapeWeight.html).
To check how many blend shapes a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) has, use the [blendShapeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-blendShapeCount.html) variable.
This code example demonstrates how to blend a default shape into two other blend shapes over time when attached to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with three or more blend shapes:
```
using UnityEngine;
using System.Collections;

public class BlendShapeExample : MonoBehaviour
{
    int blendShapeCount;
    SkinnedMeshRenderer skinnedMeshRenderer;
    Mesh skinnedMesh;
    float blendOne = 0f;
    float blendTwo = 0f;
    float blendSpeed = 1f;
    bool blendOneFinished = false;

    void Awake ()
    {
        skinnedMeshRenderer = GetComponent<SkinnedMeshRenderer> ();
        skinnedMesh = GetComponent<SkinnedMeshRenderer> ().sharedMesh;
    }

    void Start ()
    {
        blendShapeCount = skinnedMesh.blendShapeCount;
    }

    void Update ()
    {
        if (blendShapeCount > 2) {
            if (blendOne < 100f) {
                skinnedMeshRenderer.SetBlendShapeWeight (0, blendOne);
                blendOne += blendSpeed;
            } else {
                blendOneFinished = true;
            }

            if (blendOneFinished == true && blendTwo < 100f) {
                skinnedMeshRenderer.SetBlendShapeWeight (1, blendTwo);
                blendTwo += blendSpeed;
            }
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/script-AnimationWindowEvent.html)
Add an Animation Event
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AvatarCreationandSetup.html)
Humanoid Avatar
