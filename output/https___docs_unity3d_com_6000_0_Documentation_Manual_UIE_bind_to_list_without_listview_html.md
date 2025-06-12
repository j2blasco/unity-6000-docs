* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list-without-listview.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)
  * Bind to a list without ListView


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list.html)
Bind to a list with ListView
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-custom-control.html)
Bind a custom control 
# Bind to a list without ListView
**Version** : 2023.2+
You can bind to a list without ListView. To do so, bind each element to an item in the array of the serialized object and track the value of the array size. The array size might change in certain situations, such as an undo or reset operation.
This example demonstrates how to bind to a list without ListView.
## Example overview
This example creates a list of TexturePreviewElements and binds the list to an underlying list of Texture2D objects.
![A list of textures that dont use ListView, displayed in the Unity Editor.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie_bind_list_without_listview.png) A list of textures that don’t use ListView, displayed in the Unity Editor.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/2023.2/bind-to-list-without-listview).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [Visual Tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree)
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html)
  * [`TrackPropertyValue`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.TrackPropertyValue.html)
  * [`ScrollView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html)


## Create an object that contains a list
Create a C# class that contains a list. This list is the target of the binding.
  1. Create a project in Unity with any template.
  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `bind-to-list-without-ListView` to store all your files.
  3. Create a C# script named `TexturePackAsset.cs` and replace its contents with the following:

```
using System.Collections.Generic;
using UnityEngine;

namespace UIToolkitExamples
{
    [CreateAssetMenu(menuName = "UIToolkitExamples/TexturePackAsset")]
    public class TexturePackAsset : ScriptableObject
    {
        public List<Texture2D> textures;

        public void Reset()
        {
            textures = new() { null, null, null, null };
        }
    }
}

```

## Create and style a custom control
Create a custom control with C# that represents a reference to a 2D texture asset, and style it with USS.
  1. In that folder, create a folder named `Editor`.
  2. In the **Editor** folder, create a C# script named `TexturePreviewElement.cs`.
  3. Replace the contents of `TexturePreviewElement.cs` with the following:

```
using System;
using UnityEditor.UIElements;
using UnityEngine;
using UnityEngine.UIElements;
using Object = UnityEngine.Object;

namespace UIToolkitExamples
{
    [UxmlElement]
    public partial class TexturePreviewElement : BindableElement, INotifyValueChanged<Object>
    {
        public static readonly string ussClassName = "texture-preview-element";

        Image m_Preview;
        ObjectField m_ObjectField;
        Texture2D m_Value;

        public TexturePreviewElement()
        {
            AddToClassList(ussClassName);

            // Create a preview image.
            m_Preview = new Image();
            Add(m_Preview);

            // Create an ObjectField, set its object type, and register a callback when its value changes.
            m_ObjectField = new ObjectField();
            m_ObjectField.objectType = typeof(Texture2D);
            m_ObjectField.RegisterValueChangedCallback(OnObjectFieldValueChanged);
            Add(m_ObjectField);

            styleSheets.Add(Resources.Load<StyleSheet>("texture_preview_element"));
        }
        
        void OnObjectFieldValueChanged(ChangeEvent<Object> evt)
        {
            value = evt.newValue;
        }

        public void SetValueWithoutNotify(Object newValue)
        {
            if (newValue == null || newValue is Texture2D)
            {
                // Update the preview Image and update the ObjectField.
                m_Value = newValue as Texture2D;
                m_Preview.image = m_Value;
                // Notice that this line calls the ObjectField's SetValueWithoutNotify() method instead of just setting
                // m_ObjectField.value. This is very important; you don't want m_ObjectField to send a ChangeEvent.
                m_ObjectField.SetValueWithoutNotify(m_Value);
            }
            else throw new ArgumentException($"Expected object of type {typeof(Texture2D)}");
        }

        public Object value
        {
            get => m_Value;
            // The setter is called when the user changes the value of the ObjectField, which calls
            // OnObjectFieldValueChanged(), which calls this.
            set
            {
                if (value == this.value)
                    return;

                var previous = this.value;
                SetValueWithoutNotify(value);

                using (var evt = ChangeEvent<Object>.GetPooled(previous, value))
                {
                    evt.target = this;
                    SendEvent(evt);
                }
            }
        }
    }
}

```

  1. In the **Editor** folder, create a folder named `Resources`.
  2. In the **Resources** folder, create a StyleSheet named `texture_preview_element.uss` and replace its contents with the following:

```
.texture-preview-element {
    width: 200px;
    height: 200px;
}

.texture-preview-element > .unity-image {
    flex-grow: 1;
}

```

## Create the custom Editor and set the binding
Create the custom Editor with a C# script that creates the asset. 
To change the size of the textures list when the number of `TexturePreviewElements` in the UI changes, call the `SetupList()` method and walk through the list of entries in the serialized list. 
To bind each `TexturePreviewElement` to the list of textures, call [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html) with the property name of `TexturePackAsset.textures`.
  1. In the **Editor** folder, create a C# script named `TexturePackEditor.cs` and replace its contents with the following:

```
using UnityEditor;
using UnityEditor.UIElements;
using UnityEngine;
using UnityEngine.UIElements;

namespace UIToolkitExamples
{
    [CustomEditor(typeof(TexturePackAsset))]
    public class TexturePackEditor : Editor
    {
        [SerializeField]
        VisualTreeAsset m_VisualTreeAsset;

        public override VisualElement CreateInspectorGUI()
        {
            var editor = m_VisualTreeAsset.CloneTree();

            var container = editor.Q(className: "preview-container");

            SetupList(container);

            // Watch the array size to handle the list being changed        
            var propertyForSize = serializedObject.FindProperty(nameof(TexturePackAsset.textures) + ".Array");
            propertyForSize.Next(true); // Expand to obtain array size
            editor.TrackPropertyValue(propertyForSize, prop => SetupList(container));

            editor.Q<Button>("add-button").RegisterCallback<ClickEvent>(OnClick);

            return editor;
        }

        void SetupList(VisualElement container)
        {
            var property = serializedObject.FindProperty(nameof(TexturePackAsset.textures) + ".Array");

            var endProperty = property.GetEndProperty();

            property.NextVisible(true); // Expand the first child.

            var childIndex = 0;

            // Iterate each property under the array and populate the container with preview elements
            do
            {
                // Stop if we've reached the end of the array
                if (SerializedProperty.EqualContents(property, endProperty))
                    break;

                // Skip the array size property
                if (property.propertyType == SerializedPropertyType.ArraySize)
                    continue;

                TexturePreviewElement element;

                // Find an existing element or create one
                if (childIndex < container.childCount)
                {
                    element = (TexturePreviewElement)container[childIndex];
                }
                else
                {
                    element = new TexturePreviewElement();
                    container.Add(element);
                }

                element.BindProperty(property);

                ++childIndex;
            }
            while (property.NextVisible(false));   // Never expand children.

            // Remove excess elements if the array is now smaller
            while (childIndex < container.childCount)
            {
                container.RemoveAt(container.childCount - 1);
            }
        }

        void OnClick(ClickEvent evt)
        {
            var property = serializedObject.FindProperty(nameof(TexturePackAsset.textures));
            property.arraySize += 1;
            serializedObject.ApplyModifiedProperties();
        }
    }
}

```

  1. Create a UI Document called `texture_pack_editor.uxml` and replace its contents with the following:

```
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xmlns="UnityEngine.UIElements" example="UIToolkitExamples" editor-extension-mode="True">
    <ui:ScrollView>
        <ui:VisualElement class="preview-container" style="flex-wrap: wrap; flex-direction: row; justify-content: space-around;" />
    </ui:ScrollView>
    <ui:Button name="add-button" text="Add" />
</ui:UXML>

```

  1. In the Project window, select **TexturePackEditor.cs**.
  2. Drag **texture_pack_editor.uxml** to **Visual Tree Asset** in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).


## Test the binding
  1. From the menu, select **Assets** > **Create** > **UIToolkitExamples** > **TexturePackAsset**. This creates an asset named **New Texture Pack Asset**.
  2. In the Project window, select **New Texture Pack Asset**. This displays four TexturePreviewElement elements in the Inspector.
  3. Assign 2D image assets to these elements or use the **Add** button to add new elements. If you make changes in the Inspector UI, the property of the `TexturePackAsset.textures` object changes.


**Tip** : To import some textures and assign them to the different entries in the list, try this free [Playground asset store plugin](https://assetstore.unity.com/packages/essentials/tutorial-projects/unity-playground-109917).
## Additional resources
  * [SerializeObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)
  * [Bindable elements](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bindable-elements.html)
  * [Binding data type conversion](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-data-type-conversion.html)
  * [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-implementation-details.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list.html)
Bind to a list with ListView
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-custom-control.html)
Bind a custom control 
