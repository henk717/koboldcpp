import runpod

def handler(job):
    """
    This is a simple handler that takes a name as input and returns a greeting.
    The job parameter contains the input data in job["input"]
    """
    job_input = job["input"]
    
    # Return a greeting message
    return "KoboldCpp only supports pods, check https://koboldai.org/runpodcpp for the correct settings."

# Start the serverless function
runpod.serverless.start({"handler": handler})
