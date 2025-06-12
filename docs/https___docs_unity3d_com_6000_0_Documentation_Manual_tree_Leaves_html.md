* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Leaves.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * [Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Tree.html)
  * Leaf group reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Branches.html)
Branch group reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTree-landing.html)
Import trees from SpeedTree
# Leaf group reference
The leaf group generates leaves from a built-in geometry or an [imported mesh](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html).
## Using curves
You can use curves to control some properties. For more information, refer to [Editing curves](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingCurves.html). 
For many properties, the curve controls the details of the leaf’s shape along the length of the branch or trunk. 
The slider next to a curve is a multiplier on the curve values. Use the multiplier to add some variety when reusing the same curves for several leaf groups, or to fine-tune a curve’s effect. If the slider is at `0`, the curve has no impact. 
## Distribution
**Property** | **Function**  
---|---  
**Group Seed** | The randomizing seed for the leaf group. Change the seed to vary the group’s procedural generation. Note that this impacts the rotation of the leaves, but doesn’t change their distribution along the branch.  
**Frequency** | The number of leaves. Note that the final number of leaves might not equal the frequency. This variation creates a more natural look.  
**Distribution** | Gives a shape to the distribution of leaves around a parent branch. Use the curve to fine-tune the structure created by the combination of **Group Seed** and **Distribution** and to limit the leaf group to portions of the branch. For example, to prevent leaves growing near the base of a branch, move the first point of the curve to `(0.5, 0.0)`  
**Twirl** | Move all the leaves around the parent branch. Not available when you select **Random** from the **Distribution** dropdown.  
**Whorled Step** | When you select **Whorled** from the **Distribution** dropdown: how many leaves grow out of every growth point along the branch. If the leaf group has fewer leaves than the Whorled Steps value, the leaves all grow from the same point on the branch. For real plants, this is usually a Fibonacci number.  
**Growth Scale** | Use the curve to control the size of leaves relative to their position along a branch. The slider is a multiplier.  
**Growth Angle** | Use the curve to control the leaves’ angle of growth relative to their position along a branch. The slider is a multiplier.  
## Geometry
**Property** | **Function**  
---|---  
**Geometry Mode** | The shape of the leaves: ****Billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard)** for a square leaf that always faces you, **Plane** for a square leaf that can be seen from the side, and **Cross** or **TriCross** for 3D leaves. [Use a mesh](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html) for complex flowers, fruit, and other objects.  
**Material** | A material for the leaves. Not available when you select ****Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh)** from the **Geometry** list, because meshes use their own materials.  
## Shape
Adjusts the shape and growth of the leaves.
**Property** | **Function**  
---|---  
**Size** | Range for leaf size. Move the range up or down to increase or decrease the size. Move the two control points apart to widen the range for more variety. Also refer to the scaling from the **Growth Scale** property in the **Distribution** section.  
**Perpendicular Align** | How perpendicular a leaf is to its parent branch’s angle at the exact point of growth. For Geometry > Billboard, the value `1` can create an unnatural appearance, because the leaves have no other angle to give them variety.  
**Horizontal Align** | How horizontal the leaves are relative to the ground (not the branches). For Geometry > Billboard, this has no visible impact from the point of the view of the camera.  
## Wind
Increase or decrease a leaf group’s response to the **Wind Zone**. To create a Wind Zone, refer to [Animate trees with Wind Zones](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html).
Note that wind preview is available only in Play mode.
**Property** | **Function**  
---|---  
**Main Wind** | Increases the impact of the Wind Zone. A high value can make the leaves float away from the tree.  
**Main Turbulence** | Increases the impact of the Wind Zone’s turbulence on the entire object. A high value can make the leaves float away from the tree.  
**Edge Turbulence** | Increases the impact of the Wind Zone’s turbulence along the edge of the object.  
**Create Wind Zone** | Create a [Wind Zone](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)A GameObject that adds the effect of wind to your terrain. For instance, Trees within a wind zone will bend in a realistic animated fashion and the wind itself will move in pulses to create natural patterns of movement among the tree. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#windzone) **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). Note that the Wind Zone impacts all trees in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), not just trees created with this model.  
## Additional resources
  * [Mesh Renderer component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)
  * [Animate trees with Wind Zones](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)
  * [Create trees and leaves from meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Tree-From-Mesh.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tree-Branches.html)
Branch group reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SpeedTree-landing.html)
Import trees from SpeedTree
