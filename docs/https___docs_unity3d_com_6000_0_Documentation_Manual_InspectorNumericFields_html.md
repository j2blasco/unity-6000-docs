* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorNumericFields.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)
  * [Manage components and their values](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorManageComponents.html)
  * Use numeric field expressions


[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-advanced-object-picker.html)
Use the Advanced Object Picker
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorCurves.html)
Use curves
# Use numeric field expressions
Numeric field inputs accept:
  * Positive and negative numbers. Some properties might limit the range. For example, RGB values can’t be negative.
  * Mathematical expressions.
  * Special functions for multiple selections.


## Use mathematical expressions
You can use a mathematical expression to calculate the value of a numeric field.
For example, if you enter `2+3`, the field calculates the value `5` and uses it. When you change focus away from the field, the field refreshes and shows the calculated value.
For more information about supported expressions, refer to [`ExpressionEvaluator`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.html).
## Use special functions
You can use special functions to edit multiple selected objects at once. For example, a linear ramp can distribute the selected objects along an axis.
**Note** : Constrain Proportions Scale doesn’t support math mathematical for multi-selection.
### Linear
For a linear ramp between `a` and `b`, use `L(a,b)`. 
![The X field has the value L\(-10,10\). The selected capsules are evenly distributed along the x-axis from -10 to 10.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/inspector-expr-L.png) The X field has the value `L(-10,10)`. The selected capsules are evenly distributed along the x-axis from `-10` to `10`.
### Random
For random values between `a` and `b`, use `R(a,b)`.
![The X field has the value R\(-10,10\). The selected capsules are placed at random intervals along the x-axis from -10 to 10](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/inspector-expr-R.png)   

### Assign
To modify the current values, use the `+=`, `-=`, `*=`, and `/=` expressions. For example, to double the field’s value for all selected objects, enter `*=2`.
![The X field has the value /=3, which divides the randomised values from the previous example by three.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/inspector-expr-assign.png) The X field has the value `/=3`, which divides the randomised values from the previous example by three.
## Combine expressions
You can use mathematical expressions in function. For example, the expression `L(0,2*pi)` produces a linear distribution of values between `0` and `2pi`. 
The following examples uses the linear ramp function as the argument in sine and cosine functions in the X and Z fields. This distributes the objects in a circle:
![This circle was created by using cos\(L\(0,2*pi\)\)*5 for X and sin\(L\(0,2*pi\)\)*5 for Z.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/inspector-expr-trig.png) This circle was created by using `cos(L(0,2*pi))*5` for X and `sin(L(0,2*pi))*5` for Z.
## Use expressions in custom editors
When you create [custom editors](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-CustomEditors.html), support for numeric expressions are automatically available in all [`EditorGUI.PropertyField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyField.html) and [`EditorGUILayout.PropertyField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html) properties that have a numerical value.
## Additional resources
  * [Inspect scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/inspecting-scripts.html)
  * [Custom editors](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-CustomEditors.html)
  * [`ExpressionEvaluator` reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.html)
  * [`EditorGUI.PropertyField` reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyField.html)
  * [`EditorGUILayout.PropertyField` reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-advanced-object-picker.html)
Use the Advanced Object Picker
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorCurves.html)
Use curves
