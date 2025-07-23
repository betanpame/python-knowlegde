# Machine Learning Basics with Scikit-learn - Test 20

**Difficulty:** ⭐⭐⭐⭐⭐ (Hard)

## Description

Build comprehensive machine learning pipelines with advanced techniques including ensemble methods, feature engineering, hyperparameter optimization, model interpretation, and production-ready deployment strategies.

## Objectives

- Implement advanced ensemble methods and stacking
- Build sophisticated feature engineering pipelines
- Perform comprehensive hyperparameter optimization
- Create model interpretation and explainability systems
- Develop production-ready ML deployment pipelines

## Your Tasks

1. **advanced_ensemble_methods()** - Build stacking and voting classifiers
2. **feature_engineering_pipeline()** - Create automated feature engineering
3. **hyperparameter_optimization()** - Implement advanced parameter tuning
4. **model_interpretation()** - Build model explainability systems
5. **ml_production_pipeline()** - Create deployment-ready ML systems

## Example

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, make_regression, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder, PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression, Ridge, Lasso
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.inspection import permutation_importance
import joblib
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class AdvancedFeatureEngineering(BaseEstimator, TransformerMixin):
    """Custom transformer for advanced feature engineering."""
    
    def __init__(self, create_interactions=True, polynomial_degree=2, 
                 log_transform=True, binning=True, n_bins=5):
        """Initialize feature engineering parameters."""
        self.create_interactions = create_interactions
        self.polynomial_degree = polynomial_degree
        self.log_transform = log_transform
        self.binning = binning
        self.n_bins = n_bins
        self.feature_names_ = None
        self.numeric_features_ = None
        
    def fit(self, X, y=None):
        """Fit the transformer."""
        if isinstance(X, pd.DataFrame):
            self.feature_names_ = X.columns.tolist()
            self.numeric_features_ = X.select_dtypes(include=[np.number]).columns.tolist()
        else:
            self.feature_names_ = [f'feature_{i}' for i in range(X.shape[1])]
            self.numeric_features_ = self.feature_names_
        
        return self
    
    def transform(self, X):
        """Transform the features."""
        if isinstance(X, pd.DataFrame):
            X_transformed = X.copy()
        else:
            X_transformed = pd.DataFrame(X, columns=self.feature_names_)
        
        # Polynomial features
        if self.create_interactions and self.polynomial_degree > 1:
            numeric_data = X_transformed[self.numeric_features_]
            poly = PolynomialFeatures(degree=self.polynomial_degree, include_bias=False)
            poly_features = poly.fit_transform(numeric_data)
            poly_names = [f'poly_{i}' for i in range(poly_features.shape[1])]
            
            # Add polynomial features
            for i, name in enumerate(poly_names[len(self.numeric_features_):]):  # Skip original features
                X_transformed[name] = poly_features[:, len(self.numeric_features_) + i]
        
        # Log transform positive features
        if self.log_transform:
            for feature in self.numeric_features_:
                if X_transformed[feature].min() > 0:
                    X_transformed[f'{feature}_log'] = np.log1p(X_transformed[feature])
        
        # Create binned features
        if self.binning:
            for feature in self.numeric_features_:
                X_transformed[f'{feature}_binned'] = pd.cut(
                    X_transformed[feature], 
                    bins=self.n_bins, 
                    labels=False
                )
        
        # Feature interactions
        if self.create_interactions and len(self.numeric_features_) > 1:
            for i, feat1 in enumerate(self.numeric_features_):
                for feat2 in self.numeric_features_[i+1:]:
                    X_transformed[f'{feat1}_x_{feat2}'] = X_transformed[feat1] * X_transformed[feat2]
                    X_transformed[f'{feat1}_div_{feat2}'] = np.where(
                        X_transformed[feat2] != 0,
                        X_transformed[feat1] / X_transformed[feat2],
                        0
                    )
        
        return X_transformed.values

class ModelMetrics:
    """Comprehensive model evaluation metrics."""
    
    @staticmethod
    def classification_metrics(y_true, y_pred, y_pred_proba=None):
        """Calculate classification metrics."""
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted'),
            'recall': recall_score(y_true, y_pred, average='weighted'),
            'f1_score': f1_score(y_true, y_pred, average='weighted')
        }
        
        if y_pred_proba is not None:
            if y_pred_proba.shape[1] == 2:  # Binary classification
                metrics['roc_auc'] = roc_auc_score(y_true, y_pred_proba[:, 1])
            else:  # Multi-class
                metrics['roc_auc'] = roc_auc_score(y_true, y_pred_proba, multi_class='ovr')
        
        return metrics
    
    @staticmethod
    def regression_metrics(y_true, y_pred):
        """Calculate regression metrics."""
        from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
        
        return {
            'mse': mean_squared_error(y_true, y_pred),
            'mae': mean_absolute_error(y_true, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
            'r2_score': r2_score(y_true, y_pred)
        }

def advanced_ensemble_methods():
    """Implement advanced ensemble methods."""
    print("=== Advanced Ensemble Methods ===")
    
    # Load dataset
    data = load_breast_cancer()
    X, y = data.data, data.target
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Base models
    base_models = {
        'rf': RandomForestClassifier(n_estimators=100, random_state=42),
        'gb': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'svm': SVC(probability=True, random_state=42),
        'mlp': MLPClassifier(hidden_layer_sizes=(100, 50), random_state=42, max_iter=1000)
    }
    
    # Train base models and evaluate
    base_predictions = {}
    base_scores = {}
    
    for name, model in base_models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_pred_proba = model.predict_proba(X_test_scaled)
        
        metrics = ModelMetrics.classification_metrics(y_test, y_pred, y_pred_proba)
        base_scores[name] = metrics
        base_predictions[name] = y_pred_proba
        
        print(f"\\n{name.upper()} Base Model Performance:")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")
    
    # Voting Classifier (Hard and Soft Voting)
    voting_hard = VotingClassifier(
        estimators=[(name, model) for name, model in base_models.items()],
        voting='hard'
    )
    
    voting_soft = VotingClassifier(
        estimators=[(name, model) for name, model in base_models.items()],
        voting='soft'
    )
    
    # Stacking Classifier
    stacking_clf = StackingClassifier(
        estimators=[(name, model) for name, model in base_models.items()],
        final_estimator=LogisticRegression(random_state=42),
        cv=5
    )
    
    # Train ensemble methods
    ensemble_methods = {
        'Voting (Hard)': voting_hard,
        'Voting (Soft)': voting_soft,
        'Stacking': stacking_clf
    }
    
    ensemble_scores = {}
    
    for name, ensemble in ensemble_methods.items():
        ensemble.fit(X_train_scaled, y_train)
        y_pred = ensemble.predict(X_test_scaled)
        y_pred_proba = ensemble.predict_proba(X_test_scaled)
        
        metrics = ModelMetrics.classification_metrics(y_test, y_pred, y_pred_proba)
        ensemble_scores[name] = metrics
        
        print(f"\\n{name} Ensemble Performance:")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")
    
    # Compare all models
    print("\\n=== Model Comparison ===")
    all_scores = {**base_scores, **ensemble_scores}
    
    comparison_df = pd.DataFrame(all_scores).T
    print(comparison_df.round(4))
    
    # Feature importance from best model
    best_model_name = max(all_scores.keys(), key=lambda x: all_scores[x]['f1_score'])
    print(f"\\nBest Model: {best_model_name}")
    
    return base_models, ensemble_methods, all_scores

def feature_engineering_pipeline():
    """Create automated feature engineering pipeline."""
    print("\\n=== Feature Engineering Pipeline ===")
    
    # Create synthetic dataset
    X, y = make_classification(
        n_samples=1000, n_features=20, n_informative=15, 
        n_redundant=5, n_classes=2, random_state=42
    )
    
    feature_names = [f'feature_{i}' for i in range(X.shape[1])]
    X_df = pd.DataFrame(X, columns=feature_names)
    
    print(f"Original dataset shape: {X_df.shape}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_df, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Create feature engineering pipeline
    feature_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('feature_eng', AdvancedFeatureEngineering(
            create_interactions=True,
            polynomial_degree=2,
            log_transform=False,  # Data might have negative values
            binning=True,
            n_bins=5
        )),
        ('selector', SelectKBest(score_func=f_classif, k=50))  # Select top 50 features
    ])
    
    # Apply feature engineering
    X_train_engineered = feature_pipeline.fit_transform(X_train, y_train)
    X_test_engineered = feature_pipeline.transform(X_test)
    
    print(f"After feature engineering: {X_train_engineered.shape}")
    
    # Compare models with and without feature engineering
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Without feature engineering
    model.fit(X_train, y_train)
    y_pred_original = model.predict(X_test)
    y_pred_proba_original = model.predict_proba(X_test)
    metrics_original = ModelMetrics.classification_metrics(y_test, y_pred_original, y_pred_proba_original)
    
    # With feature engineering
    model.fit(X_train_engineered, y_train)
    y_pred_engineered = model.predict(X_test_engineered)
    y_pred_proba_engineered = model.predict_proba(X_test_engineered)
    metrics_engineered = ModelMetrics.classification_metrics(y_test, y_pred_engineered, y_pred_proba_engineered)
    
    print("\\nComparison of Original vs Engineered Features:")
    comparison = pd.DataFrame({
        'Original': metrics_original,
        'Engineered': metrics_engineered
    })
    print(comparison.round(4))
    
    # Feature importance analysis
    feature_importance = model.feature_importances_
    top_features_idx = np.argsort(feature_importance)[-10:][::-1]
    
    print("\\nTop 10 Most Important Features:")
    for i, idx in enumerate(top_features_idx):
        print(f"  {i+1}. Feature {idx}: {feature_importance[idx]:.4f}")
    
    return feature_pipeline, metrics_original, metrics_engineered

def hyperparameter_optimization():
    """Implement advanced hyperparameter optimization."""
    print("\\n=== Hyperparameter Optimization ===")
    
    # Load dataset
    data = load_breast_cancer()
    X, y = data.data, data.target
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Create preprocessing pipeline
    preprocessor = Pipeline([
        ('scaler', StandardScaler())
    ])
    
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    
    # Define models and their parameter spaces
    models_and_params = {
        'RandomForest': {
            'model': RandomForestClassifier(random_state=42),
            'params': {
                'n_estimators': [50, 100, 200, 300],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4],
                'max_features': ['sqrt', 'log2', None]
            }
        },
        'GradientBoosting': {
            'model': GradientBoostingClassifier(random_state=42),
            'params': {
                'n_estimators': [50, 100, 200],
                'learning_rate': [0.01, 0.1, 0.2, 0.3],
                'max_depth': [3, 5, 7, 9],
                'subsample': [0.8, 0.9, 1.0],
                'min_samples_split': [2, 5, 10]
            }
        },
        'SVM': {
            'model': SVC(random_state=42),
            'params': {
                'C': [0.1, 1, 10, 100],
                'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1],
                'kernel': ['rbf', 'poly', 'sigmoid']
            }
        }
    }
    
    optimization_results = {}
    
    for model_name, model_info in models_and_params.items():
        print(f"\\nOptimizing {model_name}...")
        
        model = model_info['model']
        param_grid = model_info['params']
        
        # Grid Search
        grid_search = GridSearchCV(
            model, param_grid, cv=5, scoring='f1_weighted', 
            n_jobs=-1, verbose=0
        )
        
        grid_search.fit(X_train_processed, y_train)
        
        # Randomized Search for comparison
        random_search = RandomizedSearchCV(
            model, param_grid, n_iter=50, cv=5, scoring='f1_weighted',
            n_jobs=-1, random_state=42, verbose=0
        )
        
        random_search.fit(X_train_processed, y_train)
        
        # Store results
        optimization_results[model_name] = {
            'grid_search': grid_search,
            'random_search': random_search,
            'grid_best_score': grid_search.best_score_,
            'random_best_score': random_search.best_score_,
            'grid_best_params': grid_search.best_params_,
            'random_best_params': random_search.best_params_
        }
        
        print(f"  Grid Search Best Score: {grid_search.best_score_:.4f}")
        print(f"  Random Search Best Score: {random_search.best_score_:.4f}")
        print(f"  Grid Search Best Params: {grid_search.best_params_}")
    
    # Test best models
    print("\\n=== Final Model Evaluation ===")
    
    best_models = {}
    for model_name, results in optimization_results.items():
        # Use the better of grid search or random search
        if results['grid_best_score'] > results['random_best_score']:
            best_model = results['grid_search'].best_estimator_
            best_score = results['grid_best_score']
        else:
            best_model = results['random_search'].best_estimator_
            best_score = results['random_best_score']
        
        # Test on holdout set
        y_pred = best_model.predict(X_test_processed)
        y_pred_proba = best_model.predict_proba(X_test_processed)
        test_metrics = ModelMetrics.classification_metrics(y_test, y_pred, y_pred_proba)
        
        best_models[model_name] = {
            'model': best_model,
            'cv_score': best_score,
            'test_metrics': test_metrics
        }
        
        print(f"\\n{model_name} - CV Score: {best_score:.4f}")
        print(f"Test Metrics:")
        for metric, value in test_metrics.items():
            print(f"  {metric}: {value:.4f}")
    
    return optimization_results, best_models

def model_interpretation():
    """Build model explainability systems."""
    print("\\n=== Model Interpretation ===")
    
    # Load dataset
    data = load_breast_cancer()
    X, y = data.data, data.target
    feature_names = data.feature_names
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("Top 10 Most Important Features:")
    print(feature_importance.head(10))
    
    # Permutation importance
    perm_importance = permutation_importance(
        model, X_test, y_test, n_repeats=10, random_state=42
    )
    
    perm_importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance_mean': perm_importance.importances_mean,
        'importance_std': perm_importance.importances_std
    }).sort_values('importance_mean', ascending=False)
    
    print("\\nTop 10 Permutation Importance Features:")
    print(perm_importance_df.head(10))
    
    # SHAP values (if available)
    try:
        import shap
        
        # Create SHAP explainer
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_test[:100])  # Sample for efficiency
        
        print("\\nSHAP Analysis Available")
        print(f"SHAP values shape: {np.array(shap_values).shape}")
        
        # Feature importance from SHAP
        if isinstance(shap_values, list):  # Multi-class
            shap_importance = np.abs(shap_values[1]).mean(0)  # Use positive class
        else:
            shap_importance = np.abs(shap_values).mean(0)
        
        shap_importance_df = pd.DataFrame({
            'feature': feature_names,
            'shap_importance': shap_importance
        }).sort_values('shap_importance', ascending=False)
        
        print("\\nTop 10 SHAP Importance Features:")
        print(shap_importance_df.head(10))
        
    except ImportError:
        print("\\nSHAP not available. Install with: pip install shap")
        shap_importance_df = None
    
    # Prediction explanation for individual samples
    print("\\n=== Individual Prediction Explanations ===")
    
    sample_idx = 0
    sample = X_test[sample_idx:sample_idx+1]
    prediction = model.predict(sample)[0]
    prediction_proba = model.predict_proba(sample)[0]
    
    print(f"Sample {sample_idx}:")
    print(f"  Actual class: {y_test[sample_idx]}")
    print(f"  Predicted class: {prediction}")
    print(f"  Prediction probabilities: {prediction_proba}")
    
    # Feature contributions for this sample
    if 'shap_values' in locals():
        if isinstance(shap_values, list):
            sample_shap = shap_values[1][sample_idx]  # Positive class
        else:
            sample_shap = shap_values[sample_idx]
        
        contribution_df = pd.DataFrame({
            'feature': feature_names,
            'value': sample.flatten(),
            'shap_contribution': sample_shap
        }).sort_values('shap_contribution', key=abs, ascending=False)
        
        print("\\nTop 10 Feature Contributions for this prediction:")
        print(contribution_df.head(10))
    
    # Model confidence analysis
    all_predictions_proba = model.predict_proba(X_test)
    max_probabilities = np.max(all_predictions_proba, axis=1)
    
    print(f"\\n=== Model Confidence Analysis ===")
    print(f"Mean prediction confidence: {np.mean(max_probabilities):.4f}")
    print(f"Std prediction confidence: {np.std(max_probabilities):.4f}")
    print(f"Min prediction confidence: {np.min(max_probabilities):.4f}")
    print(f"Max prediction confidence: {np.max(max_probabilities):.4f}")
    
    # Low confidence predictions
    low_confidence_threshold = 0.6
    low_confidence_mask = max_probabilities < low_confidence_threshold
    low_confidence_count = np.sum(low_confidence_mask)
    
    print(f"\\nPredictions with confidence < {low_confidence_threshold}: {low_confidence_count}")
    
    return feature_importance, perm_importance_df, model

def ml_production_pipeline():
    """Create deployment-ready ML pipeline."""
    print("\\n=== ML Production Pipeline ===")
    
    class MLPipeline:
        """Production-ready ML pipeline."""
        
        def __init__(self):
            """Initialize pipeline."""
            self.model = None
            self.preprocessor = None
            self.feature_selector = None
            self.metadata = {}
            self.is_trained = False
        
        def build_pipeline(self, model_type='rf'):
            """Build the ML pipeline."""
            # Preprocessing
            self.preprocessor = Pipeline([
                ('scaler', StandardScaler())
            ])
            
            # Feature selection
            self.feature_selector = SelectKBest(score_func=f_classif, k=20)
            
            # Model selection
            if model_type == 'rf':
                self.model = RandomForestClassifier(
                    n_estimators=100, max_depth=20, random_state=42
                )
            elif model_type == 'gb':
                self.model = GradientBoostingClassifier(
                    n_estimators=100, learning_rate=0.1, random_state=42
                )
            else:
                raise ValueError(f"Unknown model type: {model_type}")
            
            # Full pipeline
            self.full_pipeline = Pipeline([
                ('preprocessor', self.preprocessor),
                ('feature_selector', self.feature_selector),
                ('model', self.model)
            ])
            
            return self
        
        def train(self, X, y, validation_split=0.2):
            """Train the pipeline."""
            # Split data
            X_train, X_val, y_train, y_val = train_test_split(
                X, y, test_size=validation_split, random_state=42, stratify=y
            )
            
            # Train pipeline
            self.full_pipeline.fit(X_train, y_train)
            
            # Validation metrics
            val_predictions = self.full_pipeline.predict(X_val)
            val_predictions_proba = self.full_pipeline.predict_proba(X_val)
            val_metrics = ModelMetrics.classification_metrics(
                y_val, val_predictions, val_predictions_proba
            )
            
            # Store metadata
            self.metadata = {
                'training_date': datetime.now().isoformat(),
                'training_samples': len(X_train),
                'validation_samples': len(X_val),
                'features_used': self.feature_selector.get_support().sum(),
                'validation_metrics': val_metrics,
                'model_type': type(self.model).__name__
            }
            
            self.is_trained = True
            
            print(f"Pipeline trained successfully!")
            print(f"Validation Metrics:")
            for metric, value in val_metrics.items():
                print(f"  {metric}: {value:.4f}")
            
            return self
        
        def predict(self, X):
            """Make predictions."""
            if not self.is_trained:
                raise ValueError("Pipeline must be trained before making predictions")
            
            return self.full_pipeline.predict(X)
        
        def predict_proba(self, X):
            """Get prediction probabilities."""
            if not self.is_trained:
                raise ValueError("Pipeline must be trained before making predictions")
            
            return self.full_pipeline.predict_proba(X)
        
        def save_model(self, filepath):
            """Save the trained pipeline."""
            if not self.is_trained:
                raise ValueError("Pipeline must be trained before saving")
            
            model_data = {
                'pipeline': self.full_pipeline,
                'metadata': self.metadata
            }
            
            joblib.dump(model_data, filepath)
            print(f"Model saved to {filepath}")
        
        @classmethod
        def load_model(cls, filepath):
            """Load a trained pipeline."""
            model_data = joblib.load(filepath)
            
            instance = cls()
            instance.full_pipeline = model_data['pipeline']
            instance.metadata = model_data['metadata']
            instance.is_trained = True
            
            # Extract components
            instance.preprocessor = instance.full_pipeline.named_steps['preprocessor']
            instance.feature_selector = instance.full_pipeline.named_steps['feature_selector']
            instance.model = instance.full_pipeline.named_steps['model']
            
            print(f"Model loaded from {filepath}")
            print(f"Training date: {instance.metadata['training_date']}")
            
            return instance
        
        def get_feature_importance(self):
            """Get feature importance if available."""
            if not self.is_trained:
                raise ValueError("Pipeline must be trained first")
            
            if hasattr(self.model, 'feature_importances_'):
                # Get selected feature names
                selected_features = self.feature_selector.get_support()
                feature_names = [f'feature_{i}' for i in range(len(selected_features))]
                selected_feature_names = [name for i, name in enumerate(feature_names) if selected_features[i]]
                
                importance_df = pd.DataFrame({
                    'feature': selected_feature_names,
                    'importance': self.model.feature_importances_
                }).sort_values('importance', ascending=False)
                
                return importance_df
            else:
                return None
    
    # Demonstrate production pipeline
    data = load_breast_cancer()
    X, y = data.data, data.target
    
    # Create and train pipeline
    ml_pipeline = MLPipeline()
    ml_pipeline.build_pipeline('rf').train(X, y)
    
    # Test predictions
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    predictions = ml_pipeline.predict(X_test)
    predictions_proba = ml_pipeline.predict_proba(X_test)
    
    test_metrics = ModelMetrics.classification_metrics(y_test, predictions, predictions_proba)
    
    print(f"\\nTest Set Performance:")
    for metric, value in test_metrics.items():
        print(f"  {metric}: {value:.4f}")
    
    # Feature importance
    importance_df = ml_pipeline.get_feature_importance()
    if importance_df is not None:
        print(f"\\nTop 10 Most Important Features:")
        print(importance_df.head(10))
    
    # Save and reload model
    model_path = 'production_model.joblib'
    ml_pipeline.save_model(model_path)
    
    # Load model
    loaded_pipeline = MLPipeline.load_model(model_path)
    
    # Test loaded model
    loaded_predictions = loaded_pipeline.predict(X_test[:5])
    original_predictions = ml_pipeline.predict(X_test[:5])
    
    print(f"\\nModel consistency check:")
    print(f"Original predictions: {original_predictions}")
    print(f"Loaded predictions: {loaded_predictions}")
    print(f"Predictions match: {np.array_equal(original_predictions, loaded_predictions)}")
    
    return ml_pipeline, test_metrics

# Test all functions
if __name__ == "__main__":
    print("=== Machine Learning Production System ===")
    
    print("\\n1. Advanced Ensemble Methods:")
    ensemble_results = advanced_ensemble_methods()
    
    print("\\n" + "="*70)
    print("2. Feature Engineering Pipeline:")
    feature_results = feature_engineering_pipeline()
    
    print("\\n" + "="*70)
    print("3. Hyperparameter Optimization:")
    optimization_results = hyperparameter_optimization()
    
    print("\\n" + "="*70)
    print("4. Model Interpretation:")
    interpretation_results = model_interpretation()
    
    print("\\n" + "="*70)
    print("5. ML Production Pipeline:")
    production_results = ml_production_pipeline()
    
    print("\\n" + "="*70)
    print("=== MACHINE LEARNING SYSTEM COMPLETE ===")
    print("✓ Advanced ensemble methods with stacking and voting")
    print("✓ Automated feature engineering with selection")
    print("✓ Comprehensive hyperparameter optimization")
    print("✓ Model interpretation and explainability")
    print("✓ Production-ready ML pipeline with versioning")
    print("\\nThis system is ready for enterprise deployment!")
```

## Hints

- Use ensemble methods to combine multiple models for better performance
- Implement custom transformers for domain-specific feature engineering
- Use both grid search and random search for hyperparameter optimization
- Include model interpretation tools for explainability and trust
- Build pipelines that can be easily deployed and maintained in production

## Test Cases

Your system should:

- Implement stacking and voting classifiers that outperform base models
- Create feature engineering pipelines that improve model performance
- Perform comprehensive hyperparameter optimization with proper validation
- Provide model interpretation tools (feature importance, SHAP, etc.)
- Build production-ready pipelines with save/load functionality and metadata

## Bonus Challenge

Add model monitoring, drift detection, automated retraining, and A/B testing capabilities to create a complete MLOps system!
