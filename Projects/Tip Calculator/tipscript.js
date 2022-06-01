//Calculate Tip
function calculateTip(){
    var billAmt = document.getElementById("billamt").value;
    var serviceQua1 = document.getElementById("serviceQua1").value;
    var numOfPeople = document.getElementById("peopleamt").value;

    
    // Validate input
    if(billAmt === "" || serviceQua1 == 0){
        alert("Please enter values");
        return;
    }

    // Check if this input is empty or less than or equal to 1
    if(numOfPeople === "" || numOfPeople <=1){
        numOfPeople = 1;
        document.getElementById("each").style.display = "none";
    }else{
        document.getElementById("each").style.display = "block";
    }
    // Calculate tip
    var total = (billAmt * serviceQua1)/ numOfPeople;
    //round to two decimal places
    total = Math.round(total);
    // Display the tip
    document.getElementById("totalTip").style.display = "block";
    document.getElementById("tip").innerHTML = total;
}

// Hide the tip amount on load
document.getElementById("totalTip").style.display = "block";
document.getElementById("each").style.display = "none";

// Click to call function
document.getElementById("calculate").onclick = function(){
    calculateTip();
};
