$(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.roster-fill-in').click(function() {
		$('#modal1').openModal();
	});
	$('select').material_select();
});