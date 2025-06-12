* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-hierarchyconcept.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)
  * [Material Variants](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-landingpage.html)
  * Material Variant inheritance


[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-concept.html)
Introduction to Material Variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-tasks.html)
Create, modify, and apply Material Variants
# Material Variant inheritance
## Terminology
![Material Variant hierarchy. A parent can have one or more children.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/materialvariant-hierarchyconcept.png) Material Variant hierarchy. A parent can have one or more children. **Action** | **Explanation**  
---|---  
Reparent | To change the parent of a Material Variant.  
Override | A change to a Property of a Material Variant. Multiple changes to one Property constitute one Override.  
## How inheritance works
The effect of a change to a Material or Material Variant depends on its place in the hierarchy.
**Action** | **Recipient(s)** | **What happens**  
---|---|---  
Change a parent | Child | Any change or Override revert to a parent automatically propagates to a child.  
Change an ancestor | Child | A change to an ancestor automatically propagates to a child.  
Lock a property on a parent | Child | If you lock a Property on a parent, Unity removes all Overrides to the same Property on the child. You can no longer change that Property on the child.If you unlock the Property on the parent, Unity reapplies the Overrides it removed from the child.  
Change a child | No effect | A change to a child does not automatically propagate to its parent or ancestors.  
Change a descendant | No effect | A change to a descendant does not automatically propagate to its ancestors.  
**Apply as Override In Variant** and **Apply to Material** [Name][Name] | Parent or ancestor Material Variant | You can apply an Override upward in the hierarchy. The corresponding Property of the parent or ancestor automatically changes. You can only apply one Override at a time.  
**Apply to Material** [Name] | Parent or ancestor Material or Material Variant | You can apply an Override upward in the hierarchy. The corresponding Property of the parent or ancestor automatically changes. You can only apply one Override at a time.  
**Revert** an Override applied upward in the hierarchy or **Revert all Overrides** that are applied upward in the hierarchy | Child or descendant | The only way to revert an Override applied upward in the hierarchy is to revert this Override on the recipient parent or ancestor.  
## The Material Variant Hierarchy dialog
Here are three illustrations of the Material Variant **Hierarchy** dialog indicating the control that opens the dialog and the appearance of the different hierarchy levels.
![A Material with a child Material Variant](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/matlvariant-hierarchy-materialwithchild.png) A Material with a child Material Variant ![A Material Variant with a parent Material Variant and ancestor Material](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/matlvariant-hierarchy-onlyancestors.png) A Material Variant with a parent Material Variant and ancestor Material ![A Material Variant with a parent Material and child Material Variant](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/matlvariant-hierarchy-ancestorandchild.png) A Material Variant with a parent Material and child Material Variant
## Prevent the creation of circular dependencies or orphans
Unity prevents circular dependencies between Material Variants and provides a warning when you [delete a parent](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-tasks.html#deletematerialvariant).
**Error messages**
  * **Material** [name] **is an ancestor of** [name]. **Hierarchy cannot contain circular dependencies**.
  * **Material** [name] **has a missing parent with GUID** : [######]


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-concept.html)
Introduction to Material Variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-tasks.html)
Create, modify, and apply Material Variants
