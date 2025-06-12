* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/wizard-RagdollWizard.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Ragdoll physics](https://docs.unity3d.com/6000.0/Documentation/Manual/ragdoll-physics-section.html)
  * Create a ragdoll


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ragdoll-physics-section.html)
Ragdoll physics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RagdollStability.html)
Joint and Ragdoll stability
# Create a ragdoll
Unity has a simple wizard that lets you quickly create your own ragdoll. You simply have to drag the different limbs on the respective properties in the wizard. Then select create and Unity will automatically generate all **Colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider), **Rigidbodies** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) and **Joints** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) that make up the Ragdoll for you.
## Create the character
Ragdolls make use of **Skinned Meshes** , that is a character **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) rigged up with bones in the 3D modeling application. For this reason, you must build ragdoll characters in a 3D package like Autodesk® Maya®.
When you’ve created your character and rigged it, save the asset normally in your **Project Folder**. When you switch to Unity, you’ll see the character asset file. Select that file and the **Import Settings** dialog will appear inside the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector). Make sure that **Mesh Colliders** A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshCollider) is not enabled.
## Use the Ragdoll Wizard
It’s not possible to make the actual source asset into a ragdoll. This would require modifying the source asset file, and is therefore impossible. You will make an instance of the character asset into a ragdoll, which can then be saved as a **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) for re-use.
Create an instance of the character by dragging it from the **Project View** to the **Hierarchy View**. Expand its **Transform Hierarchy** by clicking the small arrow to the left of the instance’s name in the Hierarchy. Now you are ready to start assigning your ragdoll parts.
Open the Ragdoll Wizard by choosing **GameObject > 3D Object > Ragdoll…** from the menu bar. You will now see the Wizard itself.
![The Ragdoll Wizard](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/RagdollWizard.png) The Ragdoll Wizard
Assigning parts to the wizard should be self-explanatory. Drag the different Transforms of your character instance to the appropriate property on the wizard. This should be especially easy if you created the character asset yourself.
When you are done, click the **Create Button**. Now when you enter **Play Mode** , you will see your character go limp as a ragdoll.
The final step is to save the setup ragdoll as a Prefab. Choose **Assets - > Create -> Prefab** from the menu bar. You will see a New Prefab appear in the Project View. Rename it to “Ragdoll Prefab”. Drag the ragdoll character instance from the Hierarchy on top of the “Ragdoll Prefab”. You now have a completely set-up, re-usable ragdoll character to use as much as you like in your game.
## Note
For **Character Joints** An extended ball-socket joint which allows a joint to be limited on each axis. Mainly used for Ragdoll effects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CharacterJoint) made with the Ragdoll wizard, the joint’s **Twist** axis corresponds with the limb’s largest **swing axis** A joint property that defines the axis around which the joint can swing. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SwingAxis), the joint’s **Swing 1** axis corresponds with the limb’s smaller swing axis, and the joint’s **Swing 2** axis is for twisting the limb. This naming scheme is for legacy reasons.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ragdoll-physics-section.html)
Ragdoll physics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RagdollStability.html)
Joint and Ragdoll stability
