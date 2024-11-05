function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function navigate(path){
    window.open(path, '_top');
}