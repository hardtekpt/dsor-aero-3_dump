
"use strict";

let PlaceFeedback = require('./PlaceFeedback.js');
let PickupGoal = require('./PickupGoal.js');
let ExecuteTrajectoryActionFeedback = require('./ExecuteTrajectoryActionFeedback.js');
let PickupAction = require('./PickupAction.js');
let PickupActionGoal = require('./PickupActionGoal.js');
let MoveGroupAction = require('./MoveGroupAction.js');
let ExecuteTrajectoryAction = require('./ExecuteTrajectoryAction.js');
let PlaceActionFeedback = require('./PlaceActionFeedback.js');
let MoveGroupGoal = require('./MoveGroupGoal.js');
let PlaceResult = require('./PlaceResult.js');
let MoveGroupActionResult = require('./MoveGroupActionResult.js');
let ExecuteTrajectoryActionResult = require('./ExecuteTrajectoryActionResult.js');
let PlaceGoal = require('./PlaceGoal.js');
let PickupFeedback = require('./PickupFeedback.js');
let PickupActionResult = require('./PickupActionResult.js');
let PickupResult = require('./PickupResult.js');
let MoveGroupActionFeedback = require('./MoveGroupActionFeedback.js');
let PlaceActionGoal = require('./PlaceActionGoal.js');
let ExecuteTrajectoryActionGoal = require('./ExecuteTrajectoryActionGoal.js');
let PickupActionFeedback = require('./PickupActionFeedback.js');
let MoveGroupResult = require('./MoveGroupResult.js');
let ExecuteTrajectoryResult = require('./ExecuteTrajectoryResult.js');
let MoveGroupFeedback = require('./MoveGroupFeedback.js');
let MoveGroupActionGoal = require('./MoveGroupActionGoal.js');
let PlaceActionResult = require('./PlaceActionResult.js');
let PlaceAction = require('./PlaceAction.js');
let ExecuteTrajectoryFeedback = require('./ExecuteTrajectoryFeedback.js');
let ExecuteTrajectoryGoal = require('./ExecuteTrajectoryGoal.js');
let JointLimits = require('./JointLimits.js');
let AllowedCollisionMatrix = require('./AllowedCollisionMatrix.js');
let OrientationConstraint = require('./OrientationConstraint.js');
let OrientedBoundingBox = require('./OrientedBoundingBox.js');
let MotionPlanRequest = require('./MotionPlanRequest.js');
let ConstraintEvalResult = require('./ConstraintEvalResult.js');
let TrajectoryConstraints = require('./TrajectoryConstraints.js');
let GripperTranslation = require('./GripperTranslation.js');
let DisplayRobotState = require('./DisplayRobotState.js');
let PlaceLocation = require('./PlaceLocation.js');
let LinkPadding = require('./LinkPadding.js');
let KinematicSolverInfo = require('./KinematicSolverInfo.js');
let PlanningScene = require('./PlanningScene.js');
let VisibilityConstraint = require('./VisibilityConstraint.js');
let DisplayTrajectory = require('./DisplayTrajectory.js');
let PlanningOptions = require('./PlanningOptions.js');
let PlanningSceneWorld = require('./PlanningSceneWorld.js');
let JointConstraint = require('./JointConstraint.js');
let PositionIKRequest = require('./PositionIKRequest.js');
let CostSource = require('./CostSource.js');
let ObjectColor = require('./ObjectColor.js');
let PlannerParams = require('./PlannerParams.js');
let BoundingVolume = require('./BoundingVolume.js');
let WorkspaceParameters = require('./WorkspaceParameters.js');
let Constraints = require('./Constraints.js');
let Grasp = require('./Grasp.js');
let PlanningSceneComponents = require('./PlanningSceneComponents.js');
let RobotTrajectory = require('./RobotTrajectory.js');
let MotionPlanResponse = require('./MotionPlanResponse.js');
let RobotState = require('./RobotState.js');
let MotionPlanDetailedResponse = require('./MotionPlanDetailedResponse.js');
let AllowedCollisionEntry = require('./AllowedCollisionEntry.js');
let CollisionObject = require('./CollisionObject.js');
let PositionConstraint = require('./PositionConstraint.js');
let AttachedCollisionObject = require('./AttachedCollisionObject.js');
let MoveItErrorCodes = require('./MoveItErrorCodes.js');
let PlannerInterfaceDescription = require('./PlannerInterfaceDescription.js');
let ContactInformation = require('./ContactInformation.js');
let LinkScale = require('./LinkScale.js');

module.exports = {
  PlaceFeedback: PlaceFeedback,
  PickupGoal: PickupGoal,
  ExecuteTrajectoryActionFeedback: ExecuteTrajectoryActionFeedback,
  PickupAction: PickupAction,
  PickupActionGoal: PickupActionGoal,
  MoveGroupAction: MoveGroupAction,
  ExecuteTrajectoryAction: ExecuteTrajectoryAction,
  PlaceActionFeedback: PlaceActionFeedback,
  MoveGroupGoal: MoveGroupGoal,
  PlaceResult: PlaceResult,
  MoveGroupActionResult: MoveGroupActionResult,
  ExecuteTrajectoryActionResult: ExecuteTrajectoryActionResult,
  PlaceGoal: PlaceGoal,
  PickupFeedback: PickupFeedback,
  PickupActionResult: PickupActionResult,
  PickupResult: PickupResult,
  MoveGroupActionFeedback: MoveGroupActionFeedback,
  PlaceActionGoal: PlaceActionGoal,
  ExecuteTrajectoryActionGoal: ExecuteTrajectoryActionGoal,
  PickupActionFeedback: PickupActionFeedback,
  MoveGroupResult: MoveGroupResult,
  ExecuteTrajectoryResult: ExecuteTrajectoryResult,
  MoveGroupFeedback: MoveGroupFeedback,
  MoveGroupActionGoal: MoveGroupActionGoal,
  PlaceActionResult: PlaceActionResult,
  PlaceAction: PlaceAction,
  ExecuteTrajectoryFeedback: ExecuteTrajectoryFeedback,
  ExecuteTrajectoryGoal: ExecuteTrajectoryGoal,
  JointLimits: JointLimits,
  AllowedCollisionMatrix: AllowedCollisionMatrix,
  OrientationConstraint: OrientationConstraint,
  OrientedBoundingBox: OrientedBoundingBox,
  MotionPlanRequest: MotionPlanRequest,
  ConstraintEvalResult: ConstraintEvalResult,
  TrajectoryConstraints: TrajectoryConstraints,
  GripperTranslation: GripperTranslation,
  DisplayRobotState: DisplayRobotState,
  PlaceLocation: PlaceLocation,
  LinkPadding: LinkPadding,
  KinematicSolverInfo: KinematicSolverInfo,
  PlanningScene: PlanningScene,
  VisibilityConstraint: VisibilityConstraint,
  DisplayTrajectory: DisplayTrajectory,
  PlanningOptions: PlanningOptions,
  PlanningSceneWorld: PlanningSceneWorld,
  JointConstraint: JointConstraint,
  PositionIKRequest: PositionIKRequest,
  CostSource: CostSource,
  ObjectColor: ObjectColor,
  PlannerParams: PlannerParams,
  BoundingVolume: BoundingVolume,
  WorkspaceParameters: WorkspaceParameters,
  Constraints: Constraints,
  Grasp: Grasp,
  PlanningSceneComponents: PlanningSceneComponents,
  RobotTrajectory: RobotTrajectory,
  MotionPlanResponse: MotionPlanResponse,
  RobotState: RobotState,
  MotionPlanDetailedResponse: MotionPlanDetailedResponse,
  AllowedCollisionEntry: AllowedCollisionEntry,
  CollisionObject: CollisionObject,
  PositionConstraint: PositionConstraint,
  AttachedCollisionObject: AttachedCollisionObject,
  MoveItErrorCodes: MoveItErrorCodes,
  PlannerInterfaceDescription: PlannerInterfaceDescription,
  ContactInformation: ContactInformation,
  LinkScale: LinkScale,
};
