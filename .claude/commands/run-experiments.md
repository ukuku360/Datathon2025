# Run ML Experiments
# Usage: /run-experiments $ARGUMENTS

Set up and run machine learning experiments for: $ARGUMENTS

Execute this experimental pipeline:

1. **Experiment Setup**:
   - Define experiment parameters and hyperparameter grids
   - Set up cross-validation strategy
   - Initialize tracking for metrics

2. **Model Selection**:
   - Try multiple algorithms (Linear, Tree-based, Neural Networks)
   - Compare baseline models
   - Document model assumptions

3. **Hyperparameter Tuning**:
   - Grid search or random search
   - Track performance metrics
   - Validate on held-out set

4. **Model Evaluation**:
   - Generate performance reports
   - Create confusion matrices, ROC curves
   - Feature importance analysis

5. **Model Persistence**:
   - Save best models to `models/` directory
   - Export results to `outputs/`
   - Create experiment summary

Document everything and save artifacts with timestamps.
