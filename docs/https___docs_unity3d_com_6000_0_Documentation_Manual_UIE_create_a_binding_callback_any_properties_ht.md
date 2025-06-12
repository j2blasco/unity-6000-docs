* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-callback-any-properties.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)
  * Receive callbacks when any bound properties change


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-callback.html)
Receive callbacks when a bound property changes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list.html)
Bind to a list with ListView
# Receive callbacks when any bound properties change
**Version** : 2021.3+
The examples demonstrate how to receive callbacks when any properties of a bound serialized object changes.
## Example overview
This example creates a custom **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) with two fields. It warns the user if the values of the fields fall outside certain ranges. 
![A custom Inspector which displays a text warning in the Unity Editor.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie_bind_callback_any_properties.png) A custom Inspector which displays a text warning in the Unity Editor.
You can find the completed files for the example in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/callback-any-SerializedProperty-changes).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [`TrackSerializedObjectValue()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.TrackSerializedObjectValue.html)


## Create a Weapon object
Create a C# script to define the class `Weapon` as a `MonoBehaviour` with two properties: `m_BaseDamage` and `m_HardModeModifier`.
  1. Create a project in Unity with any template.
  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `callback-any-SerializedProperty-changes` to store your files.
  3. Create a C# script named `Weapon.cs` and replace its contents with the following:
```
using UnityEngine;

namespace UIToolkitExamples
{
    public class Weapon : MonoBehaviour
    {
        public const float maxDamage = 9999f;

        [SerializeField]
        float m_BaseDamage;

        [SerializeField]
        float m_HardModeModifier;

        public float GetDamage(bool hardMode)
        {
            return hardMode ? m_BaseDamage * m_HardModeModifier : m_BaseDamage;
        }
    }
}

```



## Create the binding to receive callbacks
Create a C# script that defines a custom Inspector for `Weapon` and uses the `TrackSerializedObjectValue()` method to check for changes in the `m_BaseDamage` and `m_HardModeModifier` properties.
  1. In the **callback-any-SerializedProperty-changes** folder, create a folder named `Editor`.
  2. In the **Editor** folder, create a C# script named `WeaponCustomEditor.cs` and replace its contents with the following:
```
using UnityEngine;
using UnityEditor;
using UnityEngine.UIElements;
using UnityEditor.UIElements;

namespace UIToolkitExamples
{
    [CustomEditor(typeof(Weapon))]
    public class WeaponCustomEditor : Editor
    {
        // This is text used for the warning labels.
        const string k_NegativeWarningText =
            "This weapon has a negative final damage on at least 1 difficulty level.";
        static readonly string k_DamageCapWarningText =
            "This weapon has an excessive final damage that is capped to " + Weapon.maxDamage +
            " on at least 1 difficulty level.";

        // These are labels to warn users about negative damage and excessive damage.
        Label m_NegativeWarning, m_DamageCapWarning;

        public override VisualElement CreateInspectorGUI()
        {
            VisualElement root = new();

            // Create FloatFields for serialized properties.
            var baseDamageField = new FloatField("Base Damage") { bindingPath = "m_BaseDamage" };
            var modifierField = new FloatField("Hard Mode Modifier") { bindingPath = "m_HardModeModifier" };
            root.Add(baseDamageField);
            root.Add(modifierField);

            // Create warning labels and style them so they stand out.
            var warnings = new VisualElement();
            m_NegativeWarning = new(k_NegativeWarningText);
            m_DamageCapWarning = new(k_DamageCapWarningText);
            warnings.style.color = Color.red;
            warnings.style.unityFontStyleAndWeight = FontStyle.Bold;
            warnings.Add(m_NegativeWarning);
            warnings.Add(m_DamageCapWarning);
            root.Add(warnings);

            // Determine whether to show the warnings at the start.
            CheckForWarnings(serializedObject);

            // Whenever any serialized property on this serialized object changes its value, call CheckForWarnings.
            root.TrackSerializedObjectValue(serializedObject, CheckForWarnings);

            return root;
        }

        // Check the current values of the serialized properties to either display or hide the warnings.
        void CheckForWarnings(SerializedObject serializedObject)
        {
            // For each possible damage values of the weapon, determine whether it's negative and whether it's above the
            // maximum damage value.
            var weapon = serializedObject.targetObject as Weapon;
            var damages = new float[] { weapon.GetDamage(true), weapon.GetDamage(false) };
            var foundNegativeDamage = false;
            var foundCappedDamage = false;
            foreach (var damage in damages)
            {
                foundNegativeDamage = foundNegativeDamage || damage < 0;
                foundCappedDamage = foundCappedDamage || damage > Weapon.maxDamage;
            }

            // Display or hide warnings depending on the values of the damages.
            m_NegativeWarning.style.display = foundNegativeDamage ? DisplayStyle.Flex : DisplayStyle.None;
            m_DamageCapWarning.style.display = foundCappedDamage ? DisplayStyle.Flex : DisplayStyle.None;
        }
    }
}

```



## Test the binding
  1. Create an empty **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  2. Select the GameObject.
  3. Add the Weapon component in the Inspector.
  4. In the **Weapon** component, change the values in the fields:
     * If **Base Damage** or **Base Damage** multiplied by **Hard Mode Modifier** is negative, a warning message appears.
     * If **Base Damage** or **Base Damage** multiplied by **Hard Mode Modifier** is greater than 9999, a different warning message appears.


## Additional resources
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)
  * [Bindable elements](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bindable-elements.html)
  * [Binding data type conversion](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-data-type-conversion.html)
  * [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-implementation-details.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-callback.html)
Receive callbacks when a bound property changes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list.html)
Bind to a list with ListView
