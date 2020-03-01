function validateForm() {

	var la = document.forms["loanForm"]["loan_amnt"].value
	var term = document.forms["loanForm"]["term"].value
	var rate = document.forms["loanForm"]["int_rate"].value
	var loe = document.forms["loanForm"]["emp_length"].value
	var ownership = document.forms["loanForm"]["home_ownership"].value
	var income = document.forms["loanForm"]["annual_inc"].value
	var verification = document.forms["loanForm"]["verification_status"].value
	var purpose = document.forms["loanForm"]["purpose"].value
	var dti = document.forms["loanForm"]["dti"].value
	var delinq2yr = document.forms["loanForm"]["delinq_2yrs"].value
	var fico = document.forms["loanForms"]["fico_range_low"].value
	var inqs = document.forms["loanForms"]["inq_last_6mths"].value
	var mthsSinceDelinq = document.forms["loanForm"]["mths_since_last_delinq"].value
	var mthsSinceRecord = document.forms["loanForm"]["mths_since_last_record"].value
	var openAccount = document.forms["loanForm"]["open_acc"].value
	var publicRecord = document.forms["loanForm"]["pub_rec"].value
	var revolvingBalance = document.forms["loanForm"]["revol_bal"].value
	var revolvingUtilization = document.forms["loanForm"]["revol_util"].value
	var totalAccount = document.forms["loanForms"]["total_acc"].value
	var collections = document.forms["loanForms"]["collections_12_mths_ex_med"].value
	var monthsSinceLastDerog = document.forms["loanForms"]["mths_since_last_major_derog"].value



	// Checking for empty boxes
	if (la == ""){
		alert("Loan Amount field cannot be empty")
		return false;
	}
	
	if (term == ""){
		alert("Term field cannot be empty")
		return false;
	}
	if (rate == ""){
		alert("rate field cannot be empty")
		return false;
	}
	if (loe == ""){
		alert("Length of employment field cannot be empty")
		return false;

	}
	if (ownership == ""){
		alert("Home Ownership field cannot be empty")
		return false;

	}
	if (income == ""){
		alert("Income field cannot be Empty")
		return false;

	}
	if (verification == ""){
		alert("Income Verification Field cannot be Empty")
		return false;

	}
	if (purpose == ""){
		alert("Loan Purpose Field cannot be Empty")
		return false;

	}
	if (dti == ""){
		alert("DTI Field cannot be Empty")
		return false;

	}
	if (delinq2yr == ""){
		alert("Field  cannot be Empty")
		return false;

	}
	if (fico == ""){
		alert("fico field  cannot be Empty")
		return false;

	}
	if (inqs == ""){
		alert("inquiries field  cannot be Empty")
		return false;

	}
	if (mthsSinceDelinq == ""){
	alert("months since last delinquency field  cannot be Empty")
	return false;

	}

	if (mthsSinceRecord == ""){
		alert("months since last public record field  cannot be Empty")
		return false;

	}

	if (openAccount == ""){
		alert("Open Accounts field  cannot be Empty")
		return false;

	}

	if (publicRecord == ""){
	alert("Public Records field  cannot be Empty")
	return false;

	}
	if (revolvingBalance == ""){
	alert("Revolving balance field  cannot be Empty")
	return false;

	}
	if (revolvingUtilization == ""){
	alert("Revolving utilization field  cannot be Empty")
	return false;

	}
	if (totalAccount == ""){
	alert("Total Accounts field  cannot be Empty")
	return false;

	}
	if (collections == ""){
	alert("Collections in past 12 months field  cannot be Empty")
	return false;

	}
	if (mths_since_last_major_derog == ""){
	alert("Months since last major derog field cannot be empty")
	return false;

	}








	

}