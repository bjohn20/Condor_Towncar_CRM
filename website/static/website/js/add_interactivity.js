$(document).ready(function () {
  const $serviceType = $("#id_service_type");
  const $pickupFields = $("#pickup-address-fields");
  const $destinationFields = $("#destination-address-fields");
  const $airportFields = $("#airport-fields");

  function toggleAddressFields() {
    const selectedValue = $serviceType.val();

    if (
      selectedValue === "PT" ||
      selectedValue === "HR" ||
      selectedValue === "OT"
    ) {
      $pickupFields.show();
      $destinationFields.show();
      $airportFields.hide();
    } else if (selectedValue === "AP") {
      $pickupFields.hide();
      $destinationFields.show();
      $airportFields.show();
    } else if (selectedValue === "AD") {
      $pickupFields.show();
      $destinationFields.hide();
      $airportFields.show();
    }
  }

  // Initial call to set the correct fields on page load
  toggleAddressFields();

  // Event listener for changes in the service type dropdown
  $serviceType.change(toggleAddressFields);
});
