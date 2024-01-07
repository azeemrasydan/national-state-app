import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable, ReplaySubject, catchError, of, tap } from "rxjs";
import { IFloodWarning } from "./flood.types";

@Injectable({ providedIn: 'root' })
export class FloodHttpService {
    private _floodWarnings: ReplaySubject<IFloodWarning[]> = new ReplaySubject<IFloodWarning[]>();
    constructor(
        private _httpClient: HttpClient
    ) { }

    set floodWarnings(floodWarnings: IFloodWarning[]) {
        this._floodWarnings?.next(floodWarnings);
    }

    get floodWarnings$() : Observable<IFloodWarning[]> {
        return this._floodWarnings.asObservable();
    }


    getFloodWarnings(): Observable<IFloodWarning[] | boolean> {
        return this._httpClient
            .get<IFloodWarning[]>('https://api.data.gov.my/flood-warning/')
            .pipe(
                catchError((res) => {
                    return of(false);
                }),
                tap((res) => {
                    if(res && res !== true){
                        this._floodWarnings.next(res);
                    }
                })
            )
    }
}