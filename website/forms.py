from django import forms
from .models import Booking, Client, Driver

US_STATES = (
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("DC", "District of Columbia"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
)


# Create Client Form
class ClientForm(forms.ModelForm):

    home_state = forms.ChoiceField(
        choices=US_STATES,
        required=True,
        initial="NY",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Client
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            # Address fields
            "home_street": forms.TextInput(attrs={"class": "form-control"}),
            "home_city": forms.TextInput(attrs={"class": "form-control"}),
            "home_zipcode": forms.TextInput(attrs={"class": "form-control"}),
            "client_notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


# Create Add Booking Form
class BookingForm(forms.ModelForm):

    # Client and Driver dropdowns
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        label="Client",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    driver = forms.ModelChoiceField(
        queryset=Driver.objects.all(),
        label="Driver",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    delegated_driver_name = forms.CharField(
        max_length=100,
        label="Delegated Driver Name",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"step": "0.01"}),
    )

    pickup_state = forms.ChoiceField(
        choices=US_STATES,
        required=True,
        initial="NY",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    destination_state = forms.ChoiceField(
        choices=US_STATES,
        required=True,
        initial="NY",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    # Vehicle Type dropdown
    vehicle_type = forms.ChoiceField(
        choices=Booking.VEHICLE_CHOICES,
        label="Vehicle Type",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    airport_code = forms.ChoiceField(
        choices=Booking.AIRPORT_CHOICES,
        label="Airport Code",
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    service_type = forms.ChoiceField(
        choices=Booking.SERVICE_CHOICES,
        label="Service Type",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If instance exists (editing), set initial values for client and driver
        if self.instance and self.instance.pk:
            self.fields["client"].initial = self.instance.client
            self.fields["driver"].initial = self.instance.driver

        if self.instance.pk is None:
            # New instance, set default service type
            self.fields["service_type"].initial = "PT"

            # Make the fields that are sometimes optional not required in the form
            self.fields["airport_code"].required = False

        # --- The crucial validation logic ---

    def clean(self):
        cleaned_data = super().clean()
        service_type = cleaned_data.get("service_type")
        airport_code = cleaned_data.get("airport_code")
        delegated_driver_name = cleaned_data.get("delegated_driver_name")

        if delegated_driver_name:
            try:
                delegated_driver_obj = Driver.objects.get(name=delegated_driver_name)
                cleaned_data["driver"] = delegated_driver_obj
            except Driver.DoesNotExist:
                pass

        # Enforce logic based on service type
        if service_type == "AP":
            # Airport Pickup logic
            if not cleaned_data.get("airport_code"):
                self.add_error(
                    "airport_code", "You must select an airport for an Airport Pickup."
                )

        elif service_type == "AD":
            # Airport Dropoff logic
            if not cleaned_data.get("pickup_street"):
                self.add_error(
                    "pickup_street",
                    "Street address is required for Airport Dropoff pickup.",
                )

        return cleaned_data

    class Meta:
        model = Booking

        # Specify the fields to include in the form
        fields = "__all__"

        widgets = {
            # Style the widgets
            "pickup_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "dropoff_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            # Dropdowns
            "delegated_driver_name": forms.TextInput(attrs={"class": "form-control"}),
            # All Address fields (Handled by model, just setting the widget class)
            "pickup_state": forms.TextInput(attrs={"class": "form-control"}),
            "pickup_zipcode": forms.TextInput(attrs={"class": "form-control"}),
            "destination_street": forms.TextInput(attrs={"class": "form-control"}),
            "destination_city": forms.TextInput(attrs={"class": "form-control"}),
            "destination_state": forms.TextInput(attrs={"class": "form-control"}),
            "destination_zipcode": forms.TextInput(attrs={"class": "form-control"}),
            # Status dropdown
            "status": forms.Select(attrs={"class": "form-select"}),
        }

        # Labels (override default labels if needed)
        labels = {
            "price": "Final Price ($)",
            "delegated_driver_name": "Delegated Driver Name (if applicable)",
        }
