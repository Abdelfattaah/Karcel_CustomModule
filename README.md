## Demo video of the task 
https://youtu.be/6UmSoPuWJpY


## Important Point

I believe that this task can be effectively achieved without converting the model from `Many2one` to `Many2many`. Doing so may not be the most suitable approach for this case, as it would allow a product to be associated with multiple brands simultaneously, which is illogical since a vehicle cannot belong to more than one brand.

Moreover, converting to Many2many may cause issues with future updates of Odoo and could conflict with custom modules that interact with the category field as `Many2one`. Instead, we can utilize a hierarchical structure where car models are subcategories of brands, and brands are subcategories under a main category (Cars).

By handling the filtering logic in the controller, we can achieve the desired functionality while maintaining the integrity of product categorizations. This method ensures a cleaner, more maintainable structure that remains compatible with future updates to Odoo.



## Overview

This project is an Odoo web application that allows users to filter cars by brand and model. It leverages Odoo's existing functionalities to manage products and categories efficiently.

## Key Components

### Models

- **ProductCategorySetup**: 
  - This model creates a hierarchical structure for car categories and subcategories. The main category "Cars" includes brands (e.g., Kia, Nissan) and their corresponding models (e.g., Cerato, Sentra).

### Controllers

- **FilterCars**:
  - Handles HTTP requests for rendering the main filter page and processing AJAX requests for filtering products based on user-selected brands and models.

### Views

- **Template (XML)**:
  - Defines the user interface, including checkboxes for brands and models, and dynamically displays the list of cars based on filters applied by the user.

### JavaScript

- Implements dynamic filtering:
  - Automatically checks model checkboxes based on the selected brand.
  - Sends AJAX requests to update the product list without reloading the page.

## Security

- **Access Control**:
  - Permissions are defined in the `ir.model.access.csv` file to manage access to product and category records, ensuring that appropriate user groups can interact with the data.

## Testing

- Unit testing should have been implemented for the custom module to ensure the correctness of the functionality. However, due to time constraints, I was unable to create these tests.

## Considerations for Production Use

- In a real-life scenario with larger data sets, it may be necessary to consider using raw SQL queries instead of the ORM. This approach could improve performance and reduce the impact of complex logic on application responsiveness, ensuring a smoother user experience.

