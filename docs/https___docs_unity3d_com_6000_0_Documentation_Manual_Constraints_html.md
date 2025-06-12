* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Constraints.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * Constraints


[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-wrecks.html)
Replace a character with a ragdoll or wreck
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AimConstraint.html)
Aim Constraint component
# Constraints
A Constraint component links the position, rotation, or scale of a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to another GameObject. A constrained GameObject moves, rotates, or scales like the GameObject it is linked to.
Unity supports the following types of Constraint components:
  * [Aim](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AimConstraint.html): Rotate the constrained GameObject to face the linked GameObject.
  * [Look At](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LookAtConstraint.html): Rotate the constrained GameObject to the linked GameObject (simplified Aim Constraint).
  * [Parent](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParentConstraint.html): Move and rotate the constrained GameObject with the linked GameObject.
  * [Position](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PositionConstraint.html): Move the constrained GameObject like the linked GameObject.
  * [Rotation](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RotationConstraint.html): Rotate the constrained GameObject like the linked GameObject.
  * [Scale](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScaleConstraint.html): Scale the constrained GameObject like the linked GameObject.


## Linking to GameObjects
Use the **Sources** list in a Constraint component to specify the GameObjects to link to.
For example, to make a crosshair follow the player’s spaceship in a 2D shooter, add a **Position Constraint** component to the crosshair. To link the crosshair to the spaceship, navigate to the **Position Constraint** component and add the spaceship GameObject to the **Sources** list. As the player moves the spaceship, the crosshair follows.
![A Position Constraint for a crosshair. The crosshair follows the player’s spaceship \(red\).](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ConstraintSourceLinking.png) A Position Constraint for a crosshair. The crosshair follows the player’s spaceship (red).
A Constraint can link to several source GameObjects. In this case, the Constraint uses the averaged position, rotation, or scale of its source GameObjects. For example, to point a Light at a group of GameObjects, add an **Aim Constraint** component to the Light GameObject. Then, add the GameObjects to illuminate in the **Sources** list. The **Aim Constraint** orients the light to face the averaged position of its sources.
Unity evaluates source GameObjects in the order that they appear in the **Sources** list. The order has no effect for the **Position** and **Scale Constraints**. However, order has an effect on **Parent** An object that contains child objects in a hierarchy. When a GameObject is a Parent of another GameObject, the Child GameObject will move, rotate, and scale exactly as its Parent does. You can think of parenting as being like the relationship between your arms and your body; whenever your body moves, your arms also move along with it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html#parent)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Parent), **Rotation** , and **Aim Constraints**. To get the result you want, reorder the **Sources** list by dragging and dropping items.
You can constrain a series of GameObjects. For example, you want ducklings to follow their mother in a row. You add a **Position Constraint** component to GameObject _Duckling1_. In the **Sources** list, you link to _MotherDuck_. You then add a **Position Constraint** to _Duckling2_ that links to _Duckling1_. As the _MotherDuck_ GameObject moves in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), _Duckling1_ follows _MotherDuck_ , and _Duckling2_ follows _Duckling1_. 
Avoid creating a cycle of Constraints, because this causes unpredictable updates during gameplay. 
## Setting Constraint properties
Use the [Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html) to change common properties in a Constraint. 
![Weight and Constraint Settings for a Position Constraint](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ConstraintSettings.png) Weight and Constraint Settings for a Position Constraint
Use **Weight** to vary the influence of a Constraint. A weight of 1 causes the Constraint to update a GameObject at the same rate as its source GameObjects. A weight of 0 removes the effect of the Constraint completely. Each source GameObject also has an individual weight.
In **Constraint Settings** , use the **At Rest** properties to specify the X, Y, and Z values to use when **Weight** is 0 or when the corresponding property in **Freeze Axes** is not checked.
Use the **Offset** properties in **Constraint Settings** to specify the X, Y, and Z values to use when constraining the GameObject. 
Use the **Freeze Axes** settings to toggle which axes the Constraint can actually modify.
## Activating and locking Constraints
There are two aspects to working with Constraints: activating and locking. 
You activate a Constraint to allow it to evaluate the position, rotation, or scale of the constrained GameObject. Unity does not evaluate inactive Constraints. 
You lock a Constraint to allow it to move, rotate, or scale the GameObject. A locked Constraint takes control of the relevant parts of the [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) of the GameObject. You cannot manually move, rotate, or scale a GameObject with a locked Constraint. You also cannot edit the **Constraint Settings**. 
To manually edit the position, rotation, or scale of a GameObject, unlock its Constraint. If the Constraint is active while unlocked, the Constraint updates **Constraint Settings** for you as you move, rotate, or scale the constrained GameObject or its source GameObjects. 
When you add a Constraint component to a GameObject, the Constraint is inactive and unlocked by default. This lets you fine-tune the position, rotation, and scale of the constrained and source GameObjects before you activate and lock the Constraint.
For convenience, the **Activate** and **Zero** buttons update **Constraint Settings** for you:
  * **Activate** : Saves the current offset from the source GameObjects, then activates and locks the constrained GameObject**.**
  * **Zero** : Resets the position, rotation, or scale to match the source GameObjects, then activates and locks the constrained GameObject. 


## Animating and combining Constraints
Use **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) to modify the source GameObjects that your constrained GameObject links to. As the animation modifies the source GameObjects, the Constraint modifies your constrained GameObject.
You can also animate properties in a Constraint component. For example, use a Parent Constraint to move a character’s sword from their hand to their back. First, add a Parent Constraint to the sword GameObject. In the **Sources** list, link the Constraint to the character’s hand and the character’s spine. To animate the sword, add **keyframes** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) for the weight of each source. To animate the sword moving from back to hand, add keyframes to change the weight of the hand from 0 to 1 with keyframes for the weight of the spine from 1 to 0.
You can add more than one kind of Constraint component to the same GameObject. When updating the GameObject, Unity evaluates Constraint components from first to last as they appear in the [Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html). A GameObject can only contain one Constraint component of the same kind. For example, you cannot add more than one Position Constraint.
## Importing Constraints
When importing FBX files into the Unity Editor from Autodesk® Maya® and MotionBuilder®, you can include Constraints. Click the [Animation tab](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html) of the Import Settings window and check **Import Constraints** :
![Import Settings with Import Constraints checked](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ConstraintImport.png) Import Settings with Import Constraints checked
For every constraint in the FBX file, Unity automatically adds a corresponding Constraint component and links it to the correct GameObjects. 
## Adding and editing Constraints
To add a Constraint component:
  1. Select the GameObject to constrain.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, click **Add Component** search for the type of Constraint you want to add, and click it to add it.
  3. To add a source GameObject to your new Constraint, drag that GameObject from the Hierarchy (or from the Scene view) into the **Sources** list.
  4. Move, rotate, or scale the constrained GameObject and its source GameObjects.
  5. To activate the Constraint, click **Activate** or **Zero** , or check **Is Active** and **Lock**.


To edit a Constraint component:
  1. Select the constrained GameObject in the Editor. 
  2. To adjust the **At Rest** or **Offset** fields, use the Inspector window to expand **Constraint Settings** , uncheck **Lock** , then edit the values.
  3. To specify the axes that the Constraint updates, expand **Constraint Settings** , then check the properties in **Freeze Axes**.
  4. To add a source GameObject to the Constraint:
     * If there are no empty slots in the Sources list, click + at the bottom of the list.
     * Drag the GameObject you want to use as a Constraint source from your scene into the **Sources** list. 
  5. To remove a source GameObject, select it in the **Sources** list and click the minus symbol (**-**) at the bottom of the list.
  6. To re-order the source GameObjects in the **Sources** list, click the double bar icon on the left side of each GameObject you want to move, and drag it up or down.
**Note:** In the **Sources** list, order has no effect on the Position, Rotation, and Scale Constraints. However, order does affect how Parent and Aim Constraints move or rotate a GameObject.
  7. Check **Is Active** and **Lock**.


* * *
  * 2018–04–11 Page published 
  * Constraints added in [2018.1](https://docs.unity3d.com/2018.1/Documentation/Manual/30_search.html?q=newin20181) NewIn20181


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs-wrecks.html)
Replace a character with a ragdoll or wreck
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AimConstraint.html)
Aim Constraint component
