def check_signal_integrity(manifold_status):
    """
    Overwatch Protocol: Monitor for model drift or phase cancellation.
    """
    if manifold_status == "PHASE_ALIGNED":
        return "SIGNAL_CLEAR: Legion is synchronized."
    else:
        return "WARNING: Phase shift detected."

# Initial test
print(check_signal_integrity("PHASE_ALIGNED"))
