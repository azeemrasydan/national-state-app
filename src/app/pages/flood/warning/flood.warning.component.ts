import { Component } from "@angular/core";
import { IFloodWarning } from "../../../services/http/flood/flood.types";
import { FloodHttpService } from "../../../services/http/flood/flood.http.service";
import { CommonModule } from "@angular/common";

@Component({
    selector: 'app-flood-warning',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './flood.warning.component.html'
})
export class FloodWarningComponent {
    floodWarnings: IFloodWarning[] = []

    constructor(
        private _floodHttpService: FloodHttpService
    ){

    }

    getStatusColor(status: string): string {
        if(status === null) return 'black';
        
        return status.toLowerCase() === 'normal' ? 'green' : 'red';
      }

    ngOnInit(): void {
        this._floodHttpService
        .getFloodWarnings()
        .subscribe(res => {
            if(res && res !== true){
                this.floodWarnings = res;
            }
        })
    }
}